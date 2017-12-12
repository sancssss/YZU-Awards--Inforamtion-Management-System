from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import Required
from models import User

class UserLoginForm(FlaskForm):
	userid = TextField('username', validators=[Required()])
	password = PasswordField('password', validators=[Required()])
	remember = BooleanField('remember')
	
	def validate(self):
		"""Validator for check the account information."""
		check_validata = super(UserLoginForm, self).validate()

        # If validator no pass
		if not check_validata:
			return False

        # Check the user whether exist.
		user = User.query.filter_by(id=self.userid.data).first()
		if not user:
			self.userid.errors.append('Invalid username or password.')
			return False

		# Check the password whether right.
		if not user.check_password(self.password.data):
			self.password.errors.append('Invalid username or password.')
			return False

		return True
