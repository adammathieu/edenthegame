from app import db
from app.models import Equipements
from exportjson import readJsonFile

data = readJsonFile('equipements.json')	#data is a list

for equipement in data:
	raw = Equipements(equipement=equipement)
	db.session.add(raw)
	db.session.commit()