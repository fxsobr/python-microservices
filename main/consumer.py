import json

import pika

from main import Produto, db

params = pika.URLParameters('amqps://zfpolbnp:T-ZXlWGfp0YxqHyBUYDe11aTZlbwe1Lt@jackal.rmq.cloudamqp.com/zfpolbnp')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(channel, method, properties, body):
    print('Recebendo no microservico main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'produto_criado':
        produto = Produto(id=data['id'], titulo=data['titulo'], image=data['imagem'])
        db.session.add(produto)
        db.session.commit()

    elif properties.content_type == 'produto_atualizado':
        produto = Produto.query.get(data['id'])
        produto.titulo = data['titulo']
        produto.image = data['imagem']
        db.session.commit()

    elif properties.content_type == 'produto_removido':
        produto = Produto.query.get(data)
        db.session.delete(produto)
        db.session.commit()


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Iniciando o consumer')

channel.start_consuming()

channel.close()
