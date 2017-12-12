from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import Required

class UserLoginForm(FlaskForm):
	username = TextField('username', validators=[Required()])
	password = PasswordField('password', validators=[Required()])
