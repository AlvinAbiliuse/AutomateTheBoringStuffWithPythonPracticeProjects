
import docx

def DocumentReturn(word):
	document = docx.Document(word)
	finalList = []
	for i in document.paragraphs:
		finalList.append(i.text)
	print('\n'.join(finalList))
	
