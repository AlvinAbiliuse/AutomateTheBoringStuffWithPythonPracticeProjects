import sys
import pyperclip
import json

try:
	jsonPass = open('passwords.json')
except FileNotFoundError:
	with open('passwords.json', 'x') as js:
		js.write(json.dumps({}))
	jsonPass = open('passwords.json')

masterPassword = 'youMeanMainPassword?'
passwords = json.loads(jsonPass.read())
if input('Enter Master Password:\n') == masterPassword:
	print('', end='')
else:
	sys.exit()
while True:
	userInput = input('Enter username or email:\n')
	if userInput in passwords.keys():
		pyperclip.copy(passwords[userInput])
		print(f'Password for {userInput} has been copied')
	else:
		print(f'Password for {userInput} is not stored!')
		if input('Would you like to save it? (y/n) \n').lower() == 'y':
			passwords[userInput] = input(f'Enter Password for {userInput}:\n')
			with open('passwords.json', 'w') as js:
				js.write(json.dumps(passwords))
			print('Password Saved!')
		else:
			print('', end='')
	if input('Try Again: (y/n):\n').lower() == 'y':
		print('', end='')
	else:
		sys.exit()
