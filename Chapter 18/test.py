import sys
import time

n = 1

while True:
	tt = 'Hello World! ' + str(n)
	sys.stdout.write(tt)
	sys.stdout.flush()
	time.sleep(1)
	sys.stdout.write('hooo')
	time.sleep(1)
	sys.stdout.write('\b' * len(tt))
	n = n + 1
