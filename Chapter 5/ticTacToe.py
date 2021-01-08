


def printBoard(board):
	print('\n  ' + board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
	print(' ---|---|---')
	print('  ' + board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
	print(' ---|---|---')
	print('  ' + board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'] + '\n')




theBoard = {'top-L': 'X', 'top-M': 'O', 'top-R': 'X',
			'mid-L': 'O', 'mid-M': 'X', 'mid-R': 'O',
			'low-L': 'X', 'low-M': 'O', 'low-R': 'X'}

printBoard(theBoard)
