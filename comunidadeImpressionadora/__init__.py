import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '4b1e93d3e5b68b9aeb014d0f3b51592a'

# Pega DATABASE_URL do Railway
database_url = os.getenv('DATABASE_URL')

# Corrige prefixo para SQLAlchemy se necessário
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

# Configura o banco (Postgres no Railway ou fallback SQLite local)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url or f"sqlite:///{os.path.join(os.path.dirname(__file__), 'comunidade.db')}"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from comunidadeImpressionadora import routes
