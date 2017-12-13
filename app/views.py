# -*- coding: utf-8 -*-
from app import app
from flask import render_template, flash, redirect, url_for
from forms import UserLoginForm
from models import User
from models import ROLE_ADMIN, ROLE_USER
from flask_login import login_required, current_user, login_user, logout_user

@app.route("/")
def main():
	"""login entrance for teachers to submit data"""
	return render_template('/index/index.html',
		title = '首页',
		ROLE_ADMIN = ROLE_ADMIN,
		ROLE_USER = ROLE_USER
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

	return render_template('/index/login.html',
		title = '登录系统',
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
@login_required
def user_centre():
	return render_template('/user/user_centre.html',
		title = '用户中心',
		)

@app.route('/adminCentre')
@login_required
def admin_centre():
	if not current_user.role == ROLE_ADMIN:
		return redirect(url_for('main'))
	return render_template('admin/admin_centre.html',
		title = '管理后台'
		)

