import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from wtforms.form import Form
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c570b5d818d9804be3b371cc13b8ce42'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kgisl@localhost/testBlog'
db = SQLAlchemy(app)
bcrypt= Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'bot.reply.kgisl@gmail.com'
app.config['MAIL_PASSWORD'] = 'DIS@2020'
mail = Mail(app)


from flaskblog import routes
