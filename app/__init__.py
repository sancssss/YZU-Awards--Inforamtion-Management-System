# -*- coding: utf-8 -*-
#设置utf8#
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#初始化flask
app = Flask(__name__)
app.config.from_object('config')

#初始化数据库
db = SQLAlchemy(app)

#初始化flask-login
lm = LoginManager()
lm.setup_app(app)
lm.login_view = "views.main"

@lm.user_loader
def load_user(user_id):
    """Load the user's info."""
    
    from models import User
    return User.query.filter_by(id=user_id).first()

from app import views, models


