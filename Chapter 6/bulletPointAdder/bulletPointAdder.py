import pyperclip

text = str(pyperclip.paste())
lines = text.split('\\n')
for i in range(len(lines)):
	lines[i] = '*' + lines[i]
print(lines)

text = ''
for i in lines:
	text = text + '\n' + i
print(text)
pyperclip.copy(text)
