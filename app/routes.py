from flask import render_template
from app import app
from app import db
from app.models import Factions,Stigmates,ProfilType

@app.route('/')
@app.route('/index')
def hello_world():
	user = {'username': 'Zagan'}
	return render_template('index.html', title='Eden The Game', user=user)

@app.route('/profils', methods=['GET','POST'])
def profils():
	user = {'username': 'Zagan'}
	factions = Factions.query.all()
	factions_list = [faction.name for faction in factions]
	return render_template('profils.html', title='Eden The Game - Cartes de profils', user=user, factions=factions_list)

@app.route('/tactiques')
def tactiques():
	user = {'username': 'Zagan'}
	return render_template('tactiques.html', title='Eden The Game - Cartes tactiques', user=user)

@app.route('/missions')
def missions():
	user = {'username': 'Zagan'}
	return render_template('missions.html', title='Eden The Game - Cartes missions', user=user)