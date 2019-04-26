from celery import Celery

app = Celery('tasks', broker='amqp://admin:admin@127.0.0.1:5672/', backend='redis://:daochi12e@127.0.0.1:6379/0')


@app.task(name='rabbitmq_test.celery.tasks.add')
def add(x, y):
    return x+y
