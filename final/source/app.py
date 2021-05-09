from flask import Flask,send_file
from flask import jsonify
from flask import request
import json
import redis
import uuid
from jobs import job, q, im, rd, add_job, generate_job_key

app = Flask(__name__)

# restore original json in redis database
@app.route('/reset', methods = ['GET'])
def reset():
	for key in rd.keys():
		rd.delete(key)
	getdata()
	return "Data Reset\n"

# create
@app.route('/create', methods = ['GET'])
def create():
	category = request.args.get('category').replace("_", " ")
	entity = request.args.get('entity').replace("_", " ")
	winner = request.args.get('winner').replace("_", " ")
	year = request.args.get('year').replace("_", " ")
	uid = str(uuid.uuid4())

	rd.hmset(uid, {"category": category, "entity": entity, "winner": winner, "year": year, "uid": uid})
	return jsonify(rd.hgetall(uid))


# read	
@app.route('/year/<year>', methods = ['GET'])
def showyear(year):
	filmlist = []
	for key in rd.keys():
		if rd.hget(key,'year') == year: 
			filmlist.append(rd.hgetall(key))	
	return "\n".join([str(x) for x in filmlist])

@app.route('/year/range', methods = ['GET'])
def showrange():
	start = request.args.get('start')
	end = request.args.get('end')
	rangelist = []
	for key in rd.keys():
		year = rd.hget(key,'year')
		if year >= start and year <= end:
			rangelist.append(rd.hgetall(key))
	
	return "\n".join([str(x) for x in rangelist])

@app.route('/year/<year>/category/<category>', methods = ['GET'])
def showyearcat(year,category):
	filmlist = []
	category = category.replace("_", " ")
	for key in rd.keys():
		if rd.hget(key,'year') == year and category == rd.hget(key,'category'):
			filmlist.append(rd.hgetall(key))
	return jsonify(filmlist)

@app.route('/uid/<uid>', methods = ['GET'])
def showuid(uid):
	return jsonify(rd.hgetall(uid))

@app.route('/entity/<entity>', methods = ['GET'])
def showname(entity):
	filmlist = []
	entity = entity.replace("_", " ")
	for key in rd.keys():
		if entity == rd.hget(key,'entity'):
			filmlist.append(rd.hgetall(key))
	return jsonify(filmlist)

# update	
@app.route('/uid/<uid>/edit', methods = ['GET'])
def edit(uid):
	elements = ['category','entity','winner','year']
	for i in request.args.keys():
		if i in elements:
			param = request.args.get(i).replace("_", " ")
			rd.hset(uid, i, param)
	return jsonify(rd.hgetall(uid))

# delete
@app.route('/year/<year>/delete', methods = ['GET'])
def deleteyear(year):
	counter = 0
	for key in rd.keys():
		if rd.hget(key,'year') == year: 
			rd.delete(key)		
			counter = counter+1	
	return "Year Deleted: " + str(counter) + " items total\n"

@app.route('/year/range/delete', methods = ['GET'])
def deleterange():
	start = request.args.get('start')
	end = request.args.get('end')
	counter = 0
	for key in rd.keys():
		year = rd.hget(key,'year')
		if year >= start and year <= end:
			rd.delete(key)		
			counter = counter+1	
	return "Range Deleted: " + str(counter) + " items total\n"

@app.route('/year/<year>/category/<category>/delete', methods = ['GET'])
def deleteyearcat(year,category):
	category = category.replace("_", " ")
	counter = 0
	for key in rd.keys():
		if rd.hget(key,'year') == year and category == rd.hget(key,'category'):
			rd.delete(key)	
			counter = counter + 1
	return "Category Deleted: " + str(counter) + " items total\n"

@app.route('/uid/<uid>/delete', methods = ['GET'])
def deleteuid(uid):
	gone = rd.hgetall(uid)
	rd.delete(uid)
	gone['status'] = "DELETED"
	return jsonify(gone)

@app.route('/entity/<entity>/delete', methods = ['GET'])
def deletename(entity):
	counter = 0
	entity = entity.replace("_", " ")
	for key in rd.keys():
		if entity == rd.hget(key,'entity'):
			rd.delete(key)	
			counter = counter+1
	return "Entity Deleted: " + str(counter) + " items total\n"

# jobs
@app.route('/jobs', methods = ['POST'])
def jobs_api():
	try:
        	job = request.get_json(force=True)
	except Exception as e:
        	return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
	return json.dumps(add_job(job['start'], job['end']))

@app.route('/check/<jid>', methods = ['GET'])
def jobscheck(jid):
	return jsonify(im.hgetall(f'job.{jid}'))

@app.route('/length', methods = ['GET'])
def queuelength():
	return str(len(q))+"\n"


@app.route('/download/<jid>', methods = ['GET'])
def jobsdownload(jid):
	if job.hget(generate_job_key(jid),"status") == 'complete':
		path = f'/app/{jid}.png'
		with open(path, 'wb') as f:
			f.write(im.hget(generate_job_key(jid), 'image'))
		return send_file(path, mimetype='image/png', as_attachment=True)

	else:
		return "job not yet finished\n"

#load json function
def getdata():
	with open("filmdata.json", "r") as json_file:
		filmjson = json.load(json_file)
	
	for film in filmjson:
		uid = str(uuid.uuid4())
		rd.hmset(uid,{'uid':uid,'category':film['category'],'entity':film['entity'],'winner':str(film['winner']),'year':film['year']})
	

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')


