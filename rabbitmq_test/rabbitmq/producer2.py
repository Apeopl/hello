import pika

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1', 5672, '/', credentials))
channel = connection.channel()
assert isinstance(channel, pika.adapters.blocking_connection.BlockingChannel)

channel.queue_declare(queue='durable', durable=True)


channel.basic_publish(exchange='',
                      routing_key='durable',
                      body='hello durable',
                      properties=pika.BasicProperties(
                          delivery_mode=2,
                      )
                      )
print(" [x] Sent 'Hello durable!'")
connection.close()
