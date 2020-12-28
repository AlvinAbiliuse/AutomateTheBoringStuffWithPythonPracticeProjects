import traceback

def spam():
	bacon()

def bacon():
	raise Exception('This is an error message')

try:
	spam()
except:
	with open('errorInfo.txt', 'a') as errorFile:
		errorFile.write(traceback.format_exc() + '\n')
	print('The traceback info was written to errorInfo.txt.')
