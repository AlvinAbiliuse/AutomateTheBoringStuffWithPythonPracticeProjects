import logging
logging.basicConfig(level=logging.DEBUG, format=f'{asctime} - {levelname} - {message}')

def factorial(n):
	logging.debug(f'Start of factorial ({n})')
	total = 1
	for i in range(n+1):
		logging.debug(f'i is {i}, total is {total}')
		total *= i
	return total

print(factorial(5))
logging.debug('End of program')
