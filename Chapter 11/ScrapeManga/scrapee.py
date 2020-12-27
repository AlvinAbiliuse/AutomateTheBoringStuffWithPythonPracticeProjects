import requests
import os

number = 1
os.mkdir('./God in School')
for i in range(100):
	os.mkdir(f'./God in School/{i+1}')
	print(i)
	while True:
		tt = requests.get(f'https://cdn2-mangaraw.me/backup/cdn_mangaraw/boss-in-school-raw/chapter-{i+1}/0{number}.jpg')
		if tt.status_code == 200:
			print(f'0{number}.jpg')
			nn = open(f'./God in School/{str(i+1)}/0{number}.jpg', 'wb')
			nn.write(tt.content)
			number+=1
		else:
			print(tt.status_code)
			number = 1
			break
