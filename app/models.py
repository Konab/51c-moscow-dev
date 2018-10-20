# from app import db


# class Employee(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	department_id = db.Column(db.Integer)
# 	chief_id = db.Column(db.Integer)
# 	name = db.Column(db.String(120))
# 	salary = db.Column(db.Integer)

# 	def __repr__(self):
# 		return 'Name: {}'.format(self.name)


# class Test_data(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	note = db.Column(db.String(120), index=True, unique=False)

# 	def __repr__(self):
# 		return 'id: {}\nnote: {}'.format(self.id, self.note)
