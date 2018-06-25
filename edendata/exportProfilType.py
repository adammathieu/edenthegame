from app import db
from app.models import ProfilType

profiltype = ['humain','mutant','janissaire','beteferoce','chaka','sorcier','dompteur','degenere','robot','familier','escorteur','pisteur','convoyeur','pasteur','seraphin'\
'hierophante','dominant','krampus','cyber','controleur','drone','bot','pyromane','soeur','esclave','inquisitrice','ordrenoire','ordrerouge','ordrevert','templiere'\
'hospitaliere','apatride','surhomme','stigmatise','alien','mort','pilote']
for type in profiltype:
	raw = ProfilType(name=type)
	db.session.add(raw)
	db.session.commit()