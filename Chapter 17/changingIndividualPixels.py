from PIL import Image

im = Image.new('RGBA', (100, 100))
for x in range(100):
	for y in range(50):
		im.putpixel((x, y), (210, 210, 210))

im.save('putpixel14.png')
