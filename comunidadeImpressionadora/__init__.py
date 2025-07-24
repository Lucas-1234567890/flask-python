from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy

app = Flask(__name__, instance_relative_config=True)

app.config['SECRET_KEY'] = '4b1e93d3e5b68b9aeb014d0f3b51592a'
if os.getenv('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
else:
    # Caminho relativo para a pasta instance, vai criar o arquivo dentro da pasta instance
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'comunidade.db')

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from comunidadeImpressionadora import models
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table('usuario'):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print('Base de dados Criado')
else:
    print('base de dados existente')

from comunidadeImpressionadora import routes
