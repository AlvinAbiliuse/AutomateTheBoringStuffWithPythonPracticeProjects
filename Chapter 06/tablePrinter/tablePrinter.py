tableData = [['apples', 'oranges', 'cherries', 'banana'],
			 ['Alice', 'Bob', 'Carol', 'David'],
			 ['dog', 'cats', 'moose', 'goose']]



def scanData(num):
	data = 0
	for i in tableData[num]:
		if len(i) > data:
			data = len(i)
	return data

def pprinttable(data, w0, w1, w2):
	order = [w0, w1, w2]
	for i in range(len(data[0])):
		for j in range(len(data)):
			print(' ' * ((order[j] - len(data[j][i]) + 1)), end='')
			print(f'{data[j][i]} ', end='')
		print('')

width0 = scanData(0)

width1 = scanData(1)

width2 = scanData(2)

pprinttable(tableData, width0, width1, width2)
