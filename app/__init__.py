# -*- coding: utf-8 -*-

#初始化flask
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

#初始化SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

#初始化flask-login
from flask_login import LoginManager
lm = LoginManager()
lm.setup_app(app)
lm.login_view = "main"

@lm.user_loader
def load_user(user_id):
    """Load the user's info."""
    from models import User
    return User.query.filter_by(id=user_id).first()

#初始化flask-admin
from flask_admin import Admin
adm = Admin(app, name='管理后台', template_mode='bootstrap3')

from app import views, models, admin


