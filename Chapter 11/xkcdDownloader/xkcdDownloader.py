import requests
import bs4

def xkcdParse():
	num = 1
	while True:
		
def xkcdDownload(link, number):
	imageData = requests.get(link)
	imageData.raise_for_status()
	with open(f'./{number}.png', 'wb') as imageFile:
		for i in imageData.iter_content(100000):
			imageFile.write(i)
	

