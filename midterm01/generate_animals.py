import petname
import random
import json
import datetime
import uuid
import redis

animal_list = [] 
rd = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

def gethead():

	headlist = ['snake', 'bull', 'lion', 'raven', 'bunny']
	num = random.randint(0, 4)
	return headlist[num]

def getbody():
	body1 = petname.generate(words = 1) 
	body2 = petname.generate(words = 1) 
	return body1 + '-' + body2

def getarms():
	return random.randrange(2,11,2)

def getlegs():
	return random.randrange(3,13,3)

def main():
	for i in range (0,100):

		uid = str(uuid.uuid4())
		head = gethead()
		body = getbody()
		arms = getarms()
		legs = getlegs()
		tails = arms+legs
		timestamp = str(datetime.datetime.now())

	
		animal = {
			'uid' : uid,
			'head' : head,
			'body' : body,
			'arms' : arms,
			'legs' : legs,
			'tails' : tails,
			'created_on' : timestamp
		}	

		animal_list.append(animal)
 


	with open('animals.json', 'w') as out:
		json.dump([animal_list], out, indent=2)

if __name__ == '__main__':
	main()

