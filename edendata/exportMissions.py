from app import db
from app.models import Missions
from exportjson import readJsonFile

data = readJsonFile('missions.json')	#data is a list

for mission in data:
	raw = Missions(mission=mission)
	db.session.add(raw)
	db.session.commit()