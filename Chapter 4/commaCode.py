lizst = []

print('Type in value to be entered or press enter to finish')
while True:
	value = input()
	if value == '':
		break
	else:
		lizst.append(value)
print(', '.join(lizst))
