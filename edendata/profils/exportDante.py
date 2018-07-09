import os
from app import db
from app.models import Profils
from exportjson import readJsonFile

directory = os.fsencode("dante")
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	print(filename)
	if filename.endswith(".json"):
		data = readJsonFile(os.path.join("dante",filename))	#data is a list
		for profil in data:
			raw = Profils(profil=profil)
			db.session.add(raw)
			db.session.commit()