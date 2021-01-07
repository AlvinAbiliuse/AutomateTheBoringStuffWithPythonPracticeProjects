from PIL import Image

im = Image.new('RGB', (1000, 1000))
turn = 0

for x in range(1000):
	for y in range(1000):
		if turn == 0:
			im.putpixel((x, y), ((x + y), 0, 0))
			turn = 1
		elif turn == 1:
			im.putpixel((x, y), (0, (x + y), 0))
			turn = 2
		elif turn == 2:
			im.putpixel((x, y), (0, 0, (x + y)))
			turn = 0

im.save('putpixel10.png')
