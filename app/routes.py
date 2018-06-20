from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def hello_world():
	user = {'username': 'Zagan'}
	return render_template('index.html', title='Eden The Game', user=user)

@app.route('/profils')
def profils():
	user = {'username': 'Zagan'}
	return render_template('profils.html', title='Eden The Game - Cartes de profils', user=user)

@app.route('/tactiques')
def tactiques():
	user = {'username': 'Zagan'}
	return render_template('tactiques.html', title='Eden The Game - Cartes tactiques', user=user)

@app.route('/missions')
def missions():
	user = {'username': 'Zagan'}
	return render_template('missions.html', title='Eden The Game - Cartes missions', user=user)