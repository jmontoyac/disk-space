import pika
import deleteFiles

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.exchange_declare(exchange='files_list', exchange_type='fanout')

result = channel.queue_declare(queue='delete_list', exclusive=False)
#queue_name = result.method.queue
queue_name = 'delete_list'

channel.queue_bind(exchange='files_list', queue=queue_name)

print('Waiting for list of files to delete')


def callback(ch, method, properties, body):
    deleteFiles.deleteFiles(body)
    #print("[x] %r" % body)

# Send list of files for deletion


channel.basic_consume(
    callback, queue=queue_name, no_ack=True
)

channel.start_consuming()
