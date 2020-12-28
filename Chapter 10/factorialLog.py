import logging
logging.basicConfig(level=logging.DEBUG, format=f'{asctime} - {levelname} - {message}')

def factorial(n):
	total = 1
	for i in range(n+1):
		total *= i
	return total

print(factorial(5))
