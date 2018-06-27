import json

def readJsonFile(file):
	""" read a json file and return the object """
	with open(file, 'r') as fp:
		obj = json.load(fp)
	return obj
