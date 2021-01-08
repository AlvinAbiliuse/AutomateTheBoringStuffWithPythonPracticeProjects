def printBoard(board):
	print('\n  ' + board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
	print(' ---|---|---')
	print('  ' + board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
	print(' ---|---|---')
	print('  ' + board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'] + '\n')

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
			'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
			'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

printBoard(theBoard)
for i in range(9):
	for i in ['X', 'O']:
		print(f'Enter Location for {i}:')
		while True:
			enteredKey = input()
			try:
				if theBoard[enteredKey] == ' ':
					theBoard[enteredKey] = i
				else:
					print('Pick an empty spot!')
					continue
				break
			except KeyError:
				print('Try Again')
		printBoard(theBoard)
