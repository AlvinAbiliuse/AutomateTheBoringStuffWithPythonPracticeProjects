#!/usr/bin/env python3

import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.debug('Start of the program')

guess = ''
while guess not in ('heads', 'tails'):
	print('Guess the coin toss! Enter Heads or tails')
	guess = input().lower()

toss = ''
if random.randint(0,1) == 0:
	toss = 'heads'
else:
	toss = 'tails'

logging.debug(f'Guess is {guess}')
logging.debug(f'toss is {toss}')

if toss == guess:
	print('You got it!')
else:
	print('Nope! Guess again!')
	guess = input()
	logging.debug(f'Second guess is {guess}')
	logging.debug(f'toss is {toss}') 
	if toss == guess:
		print('You got it!')
	else:
		print('Nope. You are really bad at this game.')
