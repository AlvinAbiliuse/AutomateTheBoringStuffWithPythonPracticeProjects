
passwords = {'alvinabiliuse@gmail.com':'tuba123tub', 'AlvinAbiliuse':'flatpak4lyf'}

userInput = input('Enter username or email\n')
if userInput in passwords.keys():
	print(f'Password for {userInput} is {passwords[userInput]}')
else:
	print(f'Password for {userInput} is not stored!')
