import os
import PyPDF2

def walkFolder(folder):
	for i in list(os.walk(folder)):
		print(i)
		for j in i[2]:
			print(j)
			if j.endswith('.pdf'):
				pdfFile = PyPDF2.PdfFileReader('%s/%s' % (i[0], j), 'rb')
				pdfWriter = PyPDF2.PdfFileWriter()
				for pageNum in range(pdfFile.numPages):
					pdfWriter.addPage(pdfFile.getPage(pageNum))

				pdfWriter.encrypt('swordfish')
				resultPdf = open('%s/_%s' % (i[0], j), 'wb')
				pdfWriter.write(resultPdf)
				resultPdf.close()

if __name__ == "__main__":
	walkFolder('./paranoidPDF')
