from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__, instance_relative_config=True)

app.config['SECRET_KEY'] = '4b1e93d3e5b68b9aeb014d0f3b51592a'

# Usa variável de ambiente DATABASE_URL (Postgres no Railway) ou fallback SQLite local
database_url = os.getenv('DATABASE_URL')
if database_url:
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'comunidade.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Evita warning

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from comunidadeImpressionadora import routes
