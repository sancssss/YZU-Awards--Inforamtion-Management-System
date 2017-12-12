# -*- coding: utf-8 -*-
from app import app
from flask import render_template, flash, redirect, url_for
from forms import UserLoginForm
from models import User
from flask_login import login_required, current_user, login_user

@app.route("/")
def main():
	"""login entrance for teachers to submit data"""
	return render_template('/index/index.html',
		title = '首页'
		)

@app.route("/userLogin", methods= ['GET', 'POST'])
def user_login():
	"""login """
	form = UserLoginForm()
	if form.validate_on_submit():
		#flash('用户名：' + form.username.data)
		#flash('pw: ' + str(form.password.data))
		user = User.query.filter_by(id=form.userid.data).one()
		login_user(user, remember=form.remember.data)
		return redirect(url_for('main'))

	return render_template('/user/login.html',
		title = '用户登录',
		form = form
		)

@app.route('/userLogout', methods=['GET', 'POST'])
def logout():
    """View function for logout."""

    # Remove the username from the cookie.
    # session.pop('username', None)

    # Using the Flask-Login to processing and check the logout status for user.
    logout_user()
    flash("You have been logged out.", category="success")
    return redirect(url_for('main'))

@app.route('/userCentre')
def user_centre():

		return render_template('/user/login.html',
		title = '用户登录',
		form = form
		)

