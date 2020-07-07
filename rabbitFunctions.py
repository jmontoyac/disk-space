import pika
import json


def publish_to_rabbit(aQueue, aBody, aHost):
    connection = pika.BlockingConnection(pika.ConnectionParameters(aHost))
    channel = connection.channel()
    channel.queue_declare(queue=aQueue)
    channel.basic_publish(exchange="",
                          routing_key=aQueue,
                          body=json.dumps(aBody, indent=4))
    connection.close()
