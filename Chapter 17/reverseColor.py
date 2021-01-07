from PIL import Image

im = Image.new('RGB', (1000, 1000))
width, height = im.size

num = 0
turn = 0
for x in range(1000):
	if turn == 3:
		turn = 0
		num +=1
	else:
		turn +=1

	for y in range(1000):
		w = (width - 1) - x
		h = (height - 1) - y
		print(f'num: {num}')
		print(f'turn: {turn}')
		im.putpixel((w, h), (num, 0, 0))

im.save('putpixel13.png')

