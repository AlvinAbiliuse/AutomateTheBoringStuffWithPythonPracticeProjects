from PIL import Image
import os

def edit(image):
	editIm = Image.open(image)
	w, h = editIm.size
	print(f'{image} width: {w}, height: {h}')
	if w > 300:
		ow = w
		w = 300
		h = h - (ow - w)
		print(f'    {image} new width: {w}, new height: {h}')

logoIm = Image.open('catlogo.png')

for i in os.listdir('./Images'):
	edit(os.path.join('Images', i))
