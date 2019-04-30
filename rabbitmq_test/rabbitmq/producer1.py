import pika


credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1', 5672, '/', credentials))
channel = connection.channel()
assert isinstance(channel, pika.adapters.blocking_connection.BlockingChannel)

# 声明queue
channel.queue_declare(queue='balance')

channel.basic_publish(exchange='', routing_key='balance', body='Hello Rabbit!')

print("[x] Sent 'Hello World!'")

connection.close()
