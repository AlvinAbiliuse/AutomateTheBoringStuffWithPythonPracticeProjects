
passwords = {'alvinabiliuse@gmail.com':'tuba123tub', 'AlvinAbiliuse':'flatpak4lyf'}

userInput = input('Username or email')
if userInput in passwords.keys():
	print(f'Password for {userInput} is {passwords[userInput]}')
else:
	print(f'Password for {userInput} is not stored!')
