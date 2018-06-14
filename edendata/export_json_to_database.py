import json
import psycopg2

def readJsonFile(file):
	""" read a json file and return the object """
	with open(file, 'r') as fp:
		obj = json.load(fp)
	return obj

def connectToDB(dbname,user):
	""" connect to database and return the cursor """
	connParams = "dbname=" + dbname + " user=" + user
	try:
		conn = psycopg2.connect(connParams)
	except:
		print("Not able to connect to database " + dbname + " with user " + user)
	cur = conn.cursor()
	return cur,conn

def insert_tactics(cursor,tactic):
	""" insert a new tactic into the tactics table """
	sql="INSERT INTO edenthegame.tactics (tactic) VALUES (%s)"
	try:
		cursor.execute(sql,(json.dumps(tactic),))
	except:
		print("Not able to execute sql request " + sql)

if __name__ == "__main__":
	cur,conn = connectToDB('hgf','postgres')
	data = readJsonFile('tactics.json')	#data is a list
	for el in data:
		insert_tactics(cur,el)
	conn.commit()
	conn.close()