

def collatz(n):
	if n == 1:
		print(str"n")
	elif n % 2 == 0:
		print(n // 2)
		collatz(n // 2)
	elif n % 2 == 1:
		print(str(3 * n + 1))
		collatz(3 * n + 1)

collatz(int(input('input number')))

