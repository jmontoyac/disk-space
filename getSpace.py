#import shutil
import pika
import psutil
import json
import os
from datetime import datetime
import awsFunctions as S3

# TODO Read value form voti.conf during installation through Ansible role
# warningLimit = ${BUCKET_WARNING_LIMIT}
warningLimit = 80.0  # Usage percentage to warn


def getDirectorySize(dir):
    total_size = 0
    start_path = '/images'  # To get size of current directory
    for path, dirs, files in os.walk(start_path):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
    size = total_size // (2**30)
    print("Directory size: " + str(size) + " GiB")
    return size


# psutil library disk info
# UNITS_MAPPING = [
#    (1<<50, ' PB'),
#    (1<<40, ' TB'),
#    (1<<30, ' GB'),
#    (1<<20, ' MB'),
#    (1<<10, ' KB'),
def getDiskInfo():
    diskInfo = psutil.disk_usage('/images')

    percent_used = (diskInfo.used * 100 / diskInfo.total)

    body_bucket = {
        "bucket_id": "buck-001",
        "date_time": str(datetime.now()),
        "total_capacity": str(diskInfo.total // (2 ** 20)),
        "total_used": str(diskInfo.used // (2 ** 20)),
        "percentage_used": str(round(percent_used, 2))
    }

    return body_bucket


def publish_to_rabbit(queue, body, host):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host))
    channel = connection.channel()
    channel.queue_declare(queue='disk_info')
    channel.basic_publish(exchange="",
                          routing_key=queue,
                          body=json.dumps(body, indent=4))
    connection.close()


body = getDiskInfo()

if float(body["percentage_used"]) >= warningLimit:
    print("Disk limit exceeded")
else:
    print("Disk limit Not yet exceeded")

# Send bucket data to Rabbit
publish_to_rabbit("disk_info", body, "rabbitmq")
