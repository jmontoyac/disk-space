#import shutil
import pika
import psutil
import json
import os
from datetime import datetime
import awsFunctions as S3

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
def getDiskInfo():
    diskInfo = psutil.disk_usage('/images')

    percent_used = (diskInfo.used * 100 / diskInfo.total)

    body_bucket = {
        "bucket_id": "buck-001",
        "date_time": str(datetime.now()),
        "total_capacity": str(diskInfo.total // (2 ** 30)),
        "total_used": str(diskInfo.used // (2 ** 30)),
        "percentage_used": str(round(percent_used, 2))
    }

    return body_bucket


def publish_to_rabbit(exchange, body, host):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host))
    channel = connection.channel()
    channel.queue_declare(queue='disk_info')
    channel.basic_publish(exchange=exchange,
                          routing_key='disk_info',
                          body=json.dumps(body, indent=4))
    connection.close()


body = getDiskInfo()

if float(body["percentage_used"]) >= warningLimit:
    print("Disk limit exceeded")
    #body["message"] = "Size Limit Exceeded"
    # S3.upload_to_aws('/images/*.jpg', 'imagesTest/*.jpg', 'voti-public')
else:
    print("Disk limit Not yet exceeded")
    #body["message"] = "Size Limit Ok"

# Send bucket data to Rabbit
publish_to_rabbit("", body, "rabbitmq")
