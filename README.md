# celery_template

1. launch an RabbitRQ service by using docker:

```
docker run -d --hostname my-rabbit --name some-rabbit -p 4369:4369 -p 5671:5671 -p5672:5672 rabbitmq
docker exec some-rabbit rabbitmqctl add_user my_user password
docker exec some-rabbit rabbitmqctl set_permissions -p / my_user ".*" ".*" ".*"
```
2. pip install celery
3. celery -A ce_tasks worker --loglevel=INFO
4. python ce_clients.py