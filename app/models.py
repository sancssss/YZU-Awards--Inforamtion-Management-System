# -*- coding: UTF-8 -*- 
from app import db

ROLE_USER = 1
ROLE_ADMIN = 0

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(32), nullable=False)
	password = db.Column(db.String(32), nullable=False)
	role = db.Column(db.SmallInteger, default = ROLE_USER)
	award_records = db.relationship('AwardRecord', backref=db.backref('users'))

	def __init__(self, id, name, password):
		self.id  = id
		self.name = name
		self.password = self.set_password(password)

	def __repr__(self):
		return unicode(self.name).encode('utf-8')

	def md5(self, str):
		import hashlib
		m = hashlib.md5()   
		m.update(str)
		print(m.hexdigest())
		return m.hexdigest()

	def set_password(self, password):
		return self.md5(password)

	def check_password(self, password):
		return (self.md5(password) == self.password)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

class Award(db.Model):
	__tablename__ = 'award'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255), nullable=False)
	institution = db.Column(db.String(255), nullable=False)
	award_records = db.relationship('AwardRecord', backref=db.backref('awards'))

	def __repr__(self):
		return unicode(self.name).encode('utf-8')

class AwardGrade(db.Model):
	__tablename__ = 'award_grade'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255), nullable=False)
	award_records = db.relationship('AwardRecord', backref=db.backref('awardgrades'))

	def __repr__(self):
		return unicode(self.name).encode('utf-8')

class AwardLevel(db.Model):
	__tablename__ = 'award_level'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255), nullable=False)
	award_records = db.relationship('AwardRecord', backref=db.backref('awardlevels'))
	
	def __repr__(self):
		return unicode(self.name).encode('utf-8')

class AwardRecord(db.Model):
	__tablename__ = 'award_record'
	record_id = db.Column(db.Integer, primary_key = True)
	award_id = db.Column(db.Integer, db.ForeignKey('award.id'), nullable=False)
	level_id = db.Column(db.Integer, db.ForeignKey('award_level.id'), nullable=False)
	grade_id = db.Column(db.Integer, db.ForeignKey('award_grade.id'), nullable=False)
	record_date = db.Column(db.String(255), nullable=False)
	award_type = db.Column(db.String(255), nullable=False)
	student_name = db.Column(db.String(255), nullable=False)
	mentor_name = db.Column(db.String(255), nullable=False)
	competition_type = db.Column(db.String(255), nullable=False)
	other_note = db.Column(db.String(255))
	submit_userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	def __repr__(self):
		return unicode(self.name).encode('utf-8')