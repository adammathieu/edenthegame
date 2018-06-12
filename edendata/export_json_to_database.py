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
	return cur

def insert_tactics(cursor,tactic):
	""" insert a new tactic into the tactics table """
	sql="INSERT INTO tactics.tactic VALUES(" + json.dumps(tactic) + ")"
	try:
		cursor.execute(sql)
	except:
		print("Not able to execute sql request " + sql)

if __name__ == "__main__":
	cur = connectToDB('hgf','postgres')
	data = readJsonFile('tactics.json')	#data is a list
	for el in data:
		insert_tactics(cur,el)