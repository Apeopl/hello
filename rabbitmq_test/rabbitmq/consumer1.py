import pika

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1', 5672, '/', credentials))
channel = connection.channel()
assert isinstance(channel, pika.adapters.blocking_connection.BlockingChannel)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue='balance', on_message_callback=callback)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
