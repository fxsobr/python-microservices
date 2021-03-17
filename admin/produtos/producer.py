import pika

params = pika.URLParameters('amqps://zfpolbnp:T-ZXlWGfp0YxqHyBUYDe11aTZlbwe1Lt@jackal.rmq.cloudamqp.com/zfpolbnp')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')
