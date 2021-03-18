import json
import pika
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "admin.settings")
django.setup()

from produtos.models import Produto

params = pika.URLParameters('amqps://zfpolbnp:T-ZXlWGfp0YxqHyBUYDe11aTZlbwe1Lt@jackal.rmq.cloudamqp.com/zfpolbnp')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(channel, method, properties, body):
    print('Recebendo no microservico admin')
    data = json.loads(body)
    print(data)
    produto = Produto.objects.get(id=data)
    produto.curtidas = produto.curtidas + 1
    produto.save()


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Iniciando o consumer')

channel.start_consuming()

channel.close()