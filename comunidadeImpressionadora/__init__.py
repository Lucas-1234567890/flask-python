from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '4b1e93d3e5b68b9aeb014d0f3b51592a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Lucas/OneDrive/site python/instance/comunidade.db'


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from comunidadeImpressionadora import routes

