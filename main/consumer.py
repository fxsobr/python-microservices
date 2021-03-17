import pika

params = pika.URLParameters('amqps://zfpolbnp:T-ZXlWGfp0YxqHyBUYDe11aTZlbwe1Lt@jackal.rmq.cloudamqp.com/zfpolbnp')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(channel, method, properties, body):
    print('Recebendo no microservico main')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback)

print('Iniciando o consumer')

channel.start_consuming()

channel.close()