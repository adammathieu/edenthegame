from app import db
from app.models import Profils
from exportjson import readJsonFile

data = readJsonFile('profils/BAMAKA.json')	#data is a list

for profil in data:
	raw = Profils(caracteristics=profil,faction_id=2)
	db.session.add(raw)
	db.session.commit()