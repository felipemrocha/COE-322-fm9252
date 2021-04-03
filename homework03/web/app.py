from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello_world():
	return "Hello, World!!!"

@app.route('/animals', methods = ['GET'])
def getanimals():
	return json.dumps(getdata())

@app.route('/animals/head/snake', methods = ['GET'])
def getsnakeheads():
	test = getdata()
	print (type(test))
	jsonList = test['animals']
	print (type(jsonList))
	output = [x for x in jsonList if x['head'] == 'snake']
	return jsonify(output)
	
@app.route('/animals/arms/6', methods = ['GET'])
def get6arms():
        test = getdata()
        print (type(test))
        jsonList = test['animals']
        print (type(jsonList))
        output = [x for x in jsonList if x['arms'] == 6]
        return jsonify(output)

def getdata():
	with open("/app/animals.json", "r") as json_file:
		userdata = json.load(json_file)
	return userdata

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
