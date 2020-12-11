import requests
import bs4

def xkcdParse():
	num = 1
	while True:
		siteData = requests.get('http://xkcd.com/' + str(num))
		print('Getting site info')
		if python.status_code == 200:
			siteBS = bs4.BeautifulSoup(siteData)
			elem = siteBS.select('#comic img')
			imgLink = elem[0].get('src')[2:]
			xkcdDownloader(imgLink, num)
			num += 1
		else:
			print('The End!')
			break


def xkcdDownloader(link, number):
	imageData = requests.get(link)
	imageData.raise_for_status()
	print(f'downloading {number}.png')
	with open(f'./{number}.png', 'wb') as imageFile:
		for i in imageData.iter_content(100000):
			imageFile.write(i)	

xkcdParse()
