import pika

credential = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1', 5672, '/', credential))
channel = connection.channel()
assert isinstance(channel, pika.adapters.blocking_connection.BlockingChannel)


channel.queue_declare(queue='durable', durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(on_message_callback=callback, queue='durable')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
