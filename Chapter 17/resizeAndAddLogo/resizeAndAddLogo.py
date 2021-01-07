from PIL import Image
import os

def edit(image):
	editIm = Image.open(image)
	w, h = editIm.size
	print(f'{image} width: {w}, height: {h}')

logoIm = Image.open('catlogo.png')

for i in os.listdir('./Images'):
	edit(os.path.join('Images', i))
