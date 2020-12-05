import PyPDF2

def bruteforce(encFile, dictionary):
	pdfFile = open(encFile, 'rb')
	dictFile = open(dictionary, 'r')
	pdfObject = PyPDF2.PdfFileReader(pdfFile)
	print('Decrypting...')
	for i in dictFile.readlines():
		if pdfObject.decrypt(i.split('\n')[0]) == 1:
			print('Password is : %s' % i.split('\n')[0])
			break
		elif pdfObject.decrypt(i.lower().split('\n')[0]) == 1:
			print('Password is : %s' % i.lower().split('\n')[0])
			break	
	print('All passwords were tested!')

bruteforce('./ss.pdf', 'dictionary.txt')
	
