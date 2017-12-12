from app import db

ROLE_USER = 1
ROLE_ADMIN = 0

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(32), nullable=False)
	password = db.Column(db.String(32), nullable=False)
	role = db.Column(db.SmallInteger, default = ROLE_USER)
	award_records = db.relationship('AwardRecord', backref = 'award_record', lazy = 'dynamic')

	def __repr__(self):
		return '<User %r>' % (self.name)

class Award(db.Model):
	__tablename__ = 'award'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255), nullable=False)
	institution = db.Column(db.String(255), nullable=False)
	award_records = db.relationship('AwardRecord', lazy = 'dynamic')

	def __repr__(self):
		return '<Award %r>' % (self.name)

class AwardGrade(db.Model):
	__tablename__ = 'award_grade'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255), nullable=False)
	award_records = db.relationship('AwardRecord', lazy = 'dynamic')

	def __repr__(self):
		return '<Award_grade %r>' % (self.name)

class AwardLevel(db.Model):
	__tablename__ = 'award_level'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255), nullable=False)
	award_records = db.relationship('AwardRecord', lazy = 'dynamic')
	
	def __repr__(self):
		return '<Award_level %r>' % (self.name)

class AwardRecord(db.Model):
	__tablename__ = 'award_record'
	record_id = db.Column(db.Integer, primary_key = True)
	award_id = db.Column(db.Integer, nullable=False, db.ForeignKey('award.id'))
	level_id = db.Column(db.Integer, nullable=False, db.ForeignKey('award_level.id'))
	grade_id = db.Column(db.Integer, nullable=False, db.ForeignKey('award_grade.id'))
	record_date = db.Column(db.String(255), nullable=False)
	award_type = db.Column(db.String(255), nullable=False)
	student_name = db.Column(db.String(255), nullable=False)
	mentor_name = db.Column(db.String(255), nullable=False)
	competition_type = db.Column(db.String(255), nullable=False)
	other_note = db.Column(db.String(255))
	submit_userid = db.Column(db.Integer, nullable=False, db.ForeignKey('user.id'))
	
	def __repr__(self):
		return '<Award %r>' % (self.name)
