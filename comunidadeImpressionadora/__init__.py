from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__, instance_relative_config=True)

app.config['SECRET_KEY'] = '4b1e93d3e5b68b9aeb014d0f3b51592a'

# Usa DATABASE_URL do Railway, senão usa SQLite local
if os.getenv('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'comunidade.db')

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from comunidadeImpressionadora import models

# Garante que todas as tabelas estão criadas
with app.app_context():
    database.create_all()
    print('Tabelas garantidas no banco')

from comunidadeImpressionadora import routes
