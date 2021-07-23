# %3 fizz
# %5 buzz
# %3 & %5 fizzBuzz

from time import sleep

def fizzbuzz():
	n = 0
	while True:
		sleep(2)
		n += 1
		print(n)
		if n % 3 == 0 and n % 5 == 0:
			print("fizzBuzz")
		elif n % 3 == 0:
			print("fizz")
		elif n % 5 == 0:
			print("buzz")

if __name__ == "__main__":
	fizzbuzz()
