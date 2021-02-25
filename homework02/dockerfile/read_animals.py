#!/usr/bin/env python3
import json
import random
import argparse
import sys

#my_parser = argparse.ArgumentParser(description='Analyze 20 animals from a random list')

#my_parser.add_argument('-r','--random',help='random animal from the list',action="store_true")
#my_parser.add_argument('-n','--number',help='specific animal from the list')
#my_parser.add_argument('-b','--breed',help='breed two random animals and generate and generate offspring',action="store_true")

#args = my_parser.parse_args()

#I ended up not using argparse for this homework but I left it here since it was working in case I want to use in in the future

def printout(num):
	print('Animal selected: ' + str(num))
	print(animals['animals'][num])

def breed(parent1, parent2):

	assert isinstance(parent1, dict), 'Input to this function should be two dictionaries'
	assert isinstance(parent2, dict), 'Input to this function should be two dictionaries'
	assert isinstance(parent2['head'], str), 'Input dictionary not according to animal'
	assert isinstance(parent2['body'], str), 'Input dictionary not according to animal'
	assert isinstance(parent2['arms'], int), 'Input dictionary not according to animal'
	assert isinstance(parent2['legs'], int), 'Input dictionary not according to animal'
	assert isinstance(parent2['tails'], int), 'Input dictionary not according to animal'
	
	rand = random.random()
	if rand>0.5:
		head = parent1['head']
	else:
		head = str(parent2['head'])

	rand = random.random()
	if rand>0.5:
		body1 = parent1['body'].partition("-")[0]
		body2 = parent2['body'].partition("-")[2]
	else:
                body1 = parent2['body'].partition("-")[0]
                body2 = parent1['body'].partition("-")[2]
	body = str(body1) + '-' + str(body2)

	arms = int((parent1['arms']+parent2['arms'])/2)
	legs = int((parent1['legs']+parent2['legs'])/2)
	tails = arms+legs

	offspring = {
		'head' : head,
		'body' : body,
		'arms' : arms,
		'legs' : legs,
		'tails' : tails
	}	

	return(f'{offspring}')
	
def main():
	with open(sys.argv[1], 'r') as f:     
    		animals = json.load(f) 

	p1 = random.randint(0,19)
	p2 = random.randint(0,19)
	while (p1 == p2):
		p2 = random.randint(0,19)
	
	print(breed(animals['animals'][p1],animals['animals'][p2]))



if __name__ == '__main__':
    main()

