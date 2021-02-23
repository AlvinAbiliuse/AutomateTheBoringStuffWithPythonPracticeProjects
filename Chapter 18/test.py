import sys
import time

n = 1

# stdout stores data which is sent to the terminal when flush() is
# called. using '\b' clears out the stored stdout data for it to be 
# filled again

while True:
	tt = 'Hello World! ' + str(n)
	sys.stdout.write(tt)
	sys.stdout.flush()
	time.sleep(1)
	sys.stdout.write('\b' * len(tt))
	n = n + 1
