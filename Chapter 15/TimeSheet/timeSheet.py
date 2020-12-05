import time
import json
import sys
import os

def changeLog(name):
	newTime = time.time()
	newLog = jsonText
	newLog[name]['time'] = newTime
	if newLog[name]['checked'] == 'in':
		newLog[name]['checked'] = 'out'
		newLog[name]['log'].insert(0, f'out:{newTime}')
		with open('./userLog.json','w') as f:
			print(f'{name}: Checked out!')
			f.write(json.dumps(newLog))
	elif newLog[name]['checked'] == 'out':
		newLog[name]['checked'] = 'in'
		newLog[name]['log'].insert(0, f'in:{newTime}')
		with open('./userLog.json','w') as f:
			print(f'{name}: Checked in!')
			f.write(json.dumps(newLog))

def addLog(name):
	newLog = jsonText
	currentTime = time.time()
	newLog[str(name)] = {'checked': 'in',
						 'time':currentTime,
						 'log':[f'in:{currentTime}']}
	print(f'{name}: Added and Checked in!')
	with open('./userLog.json', 'w') as f:
		f.write(json.dumps(newLog))

usage = 'Usage: python3 timesheet.py <option> <name>\n    -a: Add user\
\n    -c: Check User in or out\n    -l: List userlist!'
checking = os.path.exists('./userLog.json')

# def removeUser():

if __name__ == '__main__':
	if checking == False:
		with open('./userLog.json', 'w') as fileText:
			fileText.write(json.dumps({}))
	else:
		pass
	with open('./userLog.json', 'r') as f:
		lines = f.read()
		jsonText = json.loads(lines)
	try:
		if sys.argv[1] == '-a':
			if str(' '.join(sys.argv[2:])) in jsonText.keys():
				print('User already in list!')
			else:
				print(str(' '.join(sys.argv[2:])))
				addLog(str(' '.join(sys.argv[2:])))
		elif sys.argv[1] == '-c':
			if str(' '.join(sys.argv[2:])) in jsonText.keys():
				changeLog(str(' '.join(sys.argv[2:])))
			else:
				print(f'User not in list!\n{usage}')
		elif sys.argv[1] == '-l':
			print(jsonText.keys())
	except IndexError:
		print(usage)
	except Exception as e:
		print(e)



