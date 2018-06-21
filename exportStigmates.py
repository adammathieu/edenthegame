from app import db
from app.models import Stigmates

stigmates = ['destruction','ordre','protection','changement','chaos']
for stigmate in stigmates:
	raw = Stigmates(name=stigmate)
	db.session.add(raw)
	db.session.commit()
