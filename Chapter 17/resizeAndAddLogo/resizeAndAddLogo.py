from PIL import Image
import os

def resize(image):
	editIm = Image.open(os.path.join('Images', image))
	w, h = editIm.size
	if w > h:
		if w > 300:
			ow = w
			w = 300
			ratio = h / ow 
			h = int(w * ratio)
	elif h > w:
		if h > 300:
			oh = h
			h = 300
			ratio = w / oh 
			w = int(h * ratio)
	resizedImage = editIm.resize((w, h))
#	resizedImage.save(f'./Resized/{image}')
	return addLogo(resizedImage, w, h, image)
	

def addLogo(image, width, height, name):
	image.paste(logoIm, ((width - wi), (height - he)), logoIm)
	image.save(f'./Resized/{name}')

logoIm = Image.open('catlogo.png')
wi, he = logoIm.size

for i in os.listdir('./Images'):
	mainImage = resize(i)
