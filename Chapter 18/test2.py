
n = 1
while True:
	tt = 'Hello World ' + str(n)
	print(tt, end='')
	# what is flush=True for?
	print('\b' * len(tt), end='')#, flush=True)
	n = n + 1
