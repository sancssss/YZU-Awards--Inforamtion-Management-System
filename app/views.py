# -*- coding: utf-8 -*-
from app import app
from flask import render_template, flash, redirect
from forms import UserLoginForm

@app.route("/")
def main():
	"""login entrance for teachers to submit data"""
	return render_template('/index/index.html')

@app.route("/userLogin", methods= ['GET', 'POST'])
def userLogin():
	"""login """
	form = UserLoginForm()
	if form.validate_on_submit():
		flash('用户名：' + form.username.data)
		flash('pw: ' + str(form.password.data))
		return redirect('/')
	return render_template('/user/login.html',
		title = '用户登录',
		form = form
		)