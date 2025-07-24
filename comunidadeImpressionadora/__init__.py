from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__, instance_relative_config=True)

app.config['SECRET_KEY'] = '4b1e93d3e5b68b9aeb014d0f3b51592a'
# Caminho relativo para a pasta instance, vai criar o arquivo dentro da pasta instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'comunidade.db')


# Cria a pasta instance se não existir
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from comunidadeImpressionadora import routes
