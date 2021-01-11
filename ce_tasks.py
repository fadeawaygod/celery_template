from os import times
from celery import Celery
import time

app = Celery(
    "tasks",
    broker="amqp://my_user:password@192.168.99.100:5672",
    backend='rpc://',
)


@app.task
def add(x, y):
    time.sleep(1)
    return x + y


if __name__ == "__main__":
    app.start()
