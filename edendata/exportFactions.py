from app import db
from app.models import Factions

factions = ['jokers','bamaka','matriarcat','convoi','isc','horde','resistance','askaris','nephilim','angesdedante','cnj']
for faction in factions:
	raw = Factions(name=faction)
	db.session.add(raw)
	db.session.commit()