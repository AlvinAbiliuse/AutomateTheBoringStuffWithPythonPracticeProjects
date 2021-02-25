import sys

stdout_fileno = sys.stdout

sample_input = ['Hi', 'Hello', 'exit']

for ip in sample_input:
	stdout_fileno.write(ip + '\n')
