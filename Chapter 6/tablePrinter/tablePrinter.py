tableData = [['apples', 'oranges', 'cherries', 'banana'],
			 ['Alice', 'Bob', 'Carol', 'David'],
			 ['dog', 'cats', 'moose', 'goose']]



def scanData(num, data):
	for i in tableData[num]:
		if len(i) > data:
			data = len(i)

def pprinttable(data):
	for i in range(len(data[0])):
		for j in range(len(data)):
			print(f'{data[j][i]} ', end='')
		print('')

width0 = 0
scanData(0, width0)

width1 = 0
scanData(1, width1)

width2 = 0
scanData(2, width2)

pprinttable(tableData)
