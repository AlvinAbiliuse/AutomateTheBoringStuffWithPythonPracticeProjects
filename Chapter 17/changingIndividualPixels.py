from PIL import Image, ImageColor

im = Image.new('RGBA', (100, 100))
for x in range(100):
	for y in range(50):
		im.putpixel((x, y), (210, 210, 210))

for i in range(100):
	for y in range(50, 100):
		im.putpixel((x, y), ImageColor.getcolor('blue', 'RGB'))

im.save('putpixel16.png')
