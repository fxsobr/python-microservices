import requests
from dataclasses import dataclass

from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

from producer import publish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

db = SQLAlchemy(app)


@dataclass
class Produto(db.Model):
    id: int
    titulo: str
    image: str
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    titulo = db.Column(db.String(200))
    image = db.Column(db.String(200))


@dataclass
class ProdutoUsuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer)
    produto_id = db.Column(db.Integer)

    UniqueConstraint('usuario_id', 'produto_id', name='usuario_produto_unique')


@app.route('/api/produtos')
def index():
    return jsonify(Produto.query.all())


@app.route('/api/produtos/<int:id>/curtida', methods=['POST'])
def curtidas(id):
    req = requests.get('http://docker.for.mac.localhost:8000/api/usuario')
    json = req.json()
    try:
        produto_usuario = ProdutoUsuario(usuario_id=json['id'], produto_id=id)
        db.session.add(produto_usuario)
        db.session.commit()

        publish('produto_curtido', id)

    except:
        abort(400, 'Você já curtiu esse produto!')

    return jsonify({
        'mensagem': 'Sucesso'
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
