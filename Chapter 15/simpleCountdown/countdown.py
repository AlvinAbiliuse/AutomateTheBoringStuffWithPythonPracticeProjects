import time
import subprocess
from sys import argv

def countdown(time):
	print(f'Countdown Set for {str(time)}')
	time.sleep(int(time))
	print('time\'s up')
	subprocess.Popen(['see', 'alarm.wav'])

if __name__ == '__main__':
	if type(sys.argv[1]) == int:
		countdown(sys.argv[1])
