import time
import subprocess
from sys import argv

def countdown():
	try:
		print(f'Countdown Set for {argv[1]}')
		timeLeft = int(argv[1])
		while timeLeft > 0:
			time.sleep(1)
			timeLeft -= 1
		print('time\'s up')
		subprocess.Popen(['see', 'alarm.wav'])
	except IndexError:
		print(usage)

if __name__ == '__main__':
	usage = 'python3 countdown.py <seconds>'
	countdown()
