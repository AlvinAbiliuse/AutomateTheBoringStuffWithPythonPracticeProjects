from PIL import Image
import os

def edit(image):
	editIm = Image.open(os.path.join('Images', image))
	w, h = editIm.size
	print(f'{image} width: {w}, height: {h}')
#	 resize not working properly
	if w > h:
		if w > 300:
			ow = w
			w = 300
			ratio = h / ow 
			h = int(w * ratio)
			print(ratio)
			print(f'    {image} new width: {w}, new height: {h}')
	elif h > w:
		if h > 300:
			oh = h
			h = 300
			ratio = w / oh 
			w = int(h * ratio)
			print(ratio)
			print(f'    {image} new width: {w}, new height: {h}')
#	resizedImage = editIm.resize((w, h))
#	resizedImage.save(f'./Resized/{image}')

logoIm = Image.open('catlogo.png')

for i in os.listdir('./Images'):
	edit(i)
