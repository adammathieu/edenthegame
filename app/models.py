from app import db

class Factions(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)

	def __repr__(self):
		return '<Faction {}>'.format(self.name)

class Stigmates(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)

	def __repr__(self):
		return '<Stigmate {}>'.format(self.name)

class States(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)
	description = db.Column(db.Text, index=True, unique=True)

	def __repr__(self):
		return '<Stigmate {}:{}>'.format(self.name,self.description)