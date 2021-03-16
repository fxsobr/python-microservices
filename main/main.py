from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

db = SQLAlchemy(app)


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    titulo = db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProdutoUsuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer)
    produto_id = db.Column(db.Integer)

    UniqueConstraint('usuario_id', 'produto_id', name='usuario_produto_unique')


@app.route('/')
def index():
    return 'Olá Mundo'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
