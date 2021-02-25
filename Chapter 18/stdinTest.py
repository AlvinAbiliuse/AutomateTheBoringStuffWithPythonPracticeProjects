import sys

stdin_fileno = sys.stdin

for line in stdin_fileno:
	if 'exit' == line.strip():
		print('Found exit. Terminating')
		exit(0)
	else:
		print(f'Message from sys.stdin: {line}')
