# -*- coding: UTF-8 -*- 
from app import adm
from models import User, AwardRecord, Award, AwardLevel, AwardGrade
from app import db
from flask_admin.contrib.sqla import ModelView
from models import ROLE_ADMIN, ROLE_USER
from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user, login_user, logout_user
from wtforms.validators import Required

class AdminModelView(ModelView):

	def is_acessible(self):
	 	return current_user.is_authenticated and current_user.role == ROLE_ADMIN

	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('login', next=request.url))

class AwardRecordModelView(AdminModelView):
	page_size = 50
	form_args = {
    'student_name': {
        'label': '学生名字',
        'validators': [Required()]
    	}
	}


adm.add_view(AwardRecordModelView(AwardRecord, db.session()))

