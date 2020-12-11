import time
import sys

def ppStopwatch(startTime, lapTime, lapNum):
	while True:
		try:
			input()
			lap = time.time()
			print(f'Lap #{lapNum}'.ljust(5) + f'{int(lap - startTime)}'.rjust(5)  + f'({int(lap - lapTime)})'.rjust(8))
			ppStopwatch(startTime, lap, lapNum+1)
		except KeyboardInterrupt:
			print('Stopwatch Ended!')
			sys.exit()

if __name__ == "__main__":
	initialTime = time.time()
	print('Press any key to lap!')
	ppStopwatch(initialTime, initialTime, 1)
