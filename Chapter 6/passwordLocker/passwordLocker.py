import sys
import pyperclip

passwords = {'alvinabiliuse@gmail.com':'tuba123tub', 'AlvinAbiliuse':'flatpak4lyf'}

masterPassword = 'youMeanMainPassword?'

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
	if input('Try Again: (y/n):\n').lower() == 'y':
		print('', end='')
	else:
		sys.exit()
