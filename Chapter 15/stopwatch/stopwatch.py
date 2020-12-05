import time
import sys

def stopWatch(currentTime, lap):
	try:
		input()
		newTime = time.time()
		print(f'Lap {lap}')
		print(f"Time: {timeFormat(newTime-currentTime)}")
		stopWatch(newTime, (lap+1))
	except KeyboardInterrupt:
		print('Exiting..')
		sys.exit()

def timeFormat(elapsedTime):
	if elapsedTime > 3600:
		HH = elapsedTime/3600
		MM = float('.' + str(HH).split('.')[1]) * 60
		SS = float('.' + str(MM).split('.')[1]) * 60
		return f'{round(HH)} Hours, {round(MM)} Minutes, {round(SS)} Seconds!'
	elif elapsedTime > 60:
		MM = elapsedTime/60
		SS = float('.' + str(MM).split('.')[1]) * 60
		return f'{round(MM)} Minutes, {round(SS)} Seconds!'
	else:
		return f'{round(elapsedTime)} Seconds!'

if __name__ == "__main__":
	print('Stopwatch Started; Press Enter to Lap and Ctrl+C to stop')
	stopWatch(time.time(), 1)
