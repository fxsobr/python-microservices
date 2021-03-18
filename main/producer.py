import json

import pika

params = pika.URLParameters('amqps://zfpolbnp:T-ZXlWGfp0YxqHyBUYDe11aTZlbwe1Lt@jackal.rmq.cloudamqp.com/zfpolbnp')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
