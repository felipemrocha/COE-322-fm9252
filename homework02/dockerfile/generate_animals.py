#!/usr/bin/env python3
import petname
import random
import json
import sys

animal_list = [] 

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

i = 1
while (i <=20):

	animal = {
		'head' : gethead(),
		'body' : getbody(),
		'arms' : getarms(),
		'legs' : getlegs()
	}	

	animal['tails'] = animal['arms']+ animal['legs']

	unique = True

	for animalcheck in animal_list:
		if(animalcheck == animal):
			unique = False
			break


	if (unique):
		animal_list.append(animal)
		i+=1

with open(sys.argv[1], 'w') as f:          
	json.dump({'animals' : animal_list}, f, indent=2)

