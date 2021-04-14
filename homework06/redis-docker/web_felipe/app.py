from flask import Flask
from flask import jsonify
from flask import request
import json
import redis
import datetime
import os

app = Flask(__name__)
redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()
rd=redis.StrictRedis(host=redis_ip, port=6379, db=0, decode_responses=True)

@app.route('/reset', methods = ['GET'])
def reset():
	for key in rd.keys():
		rd.delete(key)
	getdata()
	return "Data Reset\n"
	
@app.route('/animals', methods = ['GET'])
def getanimals():
	animallist = []
	for key in rd.keys():
		animallist.append(rd.hgetall(key))
	return jsonify(animallist)

@app.route('/animals/<uid>', methods = ['GET'])
def showanimal(uid):
	return jsonify(rd.hgetall(uid))

@app.route('/animals/dates/range', methods = ['GET'])
def showrange():
	start = request.args.get('start')
	end = request.args.get('end')
	startdate = datetime.datetime.strptime(start, "'%Y-%m-%d_%H:%M:%S.%f'")
	enddate = datetime.datetime.strptime(end, "'%Y-%m-%d_%H:%M:%S.%f'")
	rangelist = []
	for key in rd.keys():
		time = datetime.datetime.strptime(rd.hget(key,'created_on'), '%Y-%m-%d %H:%M:%S.%f')
		if time >= startdate and time <= enddate:
			rangelist.append(rd.hgetall(key))
	return jsonify(rangelist)
	
@app.route('/animals/<uid>/edit', methods = ['GET'])
def edit(uid):
	features = ['head','body','arms','legs','tails']
	for i in request.args.keys():
		if i in features:
			rd.hset(uid, i, request.args.get(i))
	return "Animal Edited\n"


@app.route('/animals/dates/delete', methods = ['GET'])
def deleterange():
	start = request.args.get('start')
	end = request.args.get('end')
	startdate = datetime.datetime.strptime(start, "'%Y-%m-%d_%H:%M:%S.%f'")
	enddate = datetime.datetime.strptime(end, "'%Y-%m-%d_%H:%M:%S.%f'")
	for key in rd.keys():
		time = datetime.datetime.strptime(rd.hget(key,'created_on'), '%Y-%m-%d %H:%M:%S.%f')
		if time >= startdate and time <= enddate:
			rd.delete(key)
	return "Range Deleted\n"
	
@app.route('/animals/legs/average', methods = ['GET'])
def avglegs():
	sum = 0
	count = 0
	for key in rd.keys():
		sum = sum + int(rd.hget(key,'legs'))
		count = count + 1
	avg = round(sum/count,3)
	return str(avg)+'\n'

@app.route('/animals/count', methods = ['GET'])
def count():
	count = 0
	for key in rd.keys():
		count = count + 1
	return str(count)+'\n'

def getdata():
	with open("animals.json", "r") as json_file:
		animaljson = json.load(json_file)
	for animal in animaljson:
		rd.hmset(animal['uid'],animal)
	

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5027)
