import pika

credentials = pika.PlainCredentials(username='my_user', password='password')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.99.100', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()