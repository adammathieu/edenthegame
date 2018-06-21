from app import db
from sqlalchemy.dialects.postgresql import JSON

class Factions(db.Model):
	__tablename__ = 'factions'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)

	def __init__(self,name):
		self.name = name

	def __repr__(self):
		return '<Faction {}>'.format(self.name)

class Stigmates(db.Model):
	__tablename__ = 'stigmates'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)

	def __init__(self,name):
		self.name = name

	def __repr__(self):
		return '<Stigmate {}>'.format(self.name)

class States(db.Model):
	__tablename__ = 'states'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)
	description = db.Column(db.Text, index=True, unique=True)

	def __init__(self,name,description):
		self.name = name
		self.description = description

	def __repr__(self):
		return '<Etat {}:{}>'.format(self.name,self.description)

class Missions(db.Model):
	__tablename__ = 'missions'

	id = db.Column(db.Integer, primary_key=True)
	mission = db.Column(JSON)

	def __init__(self,mission):
		self.mission = mission

	def __repr__(self):
		return '<id {}>'.format(self.id)

class Tactiques(db.Model):
	__tablename__ = 'tactics'

	id = db.Column(db.Integer, primary_key=True)
	tactique = db.Column(JSON)

	def __init__(self,tactique):
		self.tactique = tactique

	def __repr__(self):
		return '<id {}>'.format(self.id)

class ProfilType(db.Model):
	__tablename__ = 'profiltype'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)

	def __init__(self,name):
		self.name = name

	def __repr__(self):
		return '<Type de Profil {}>'.format(self.name)