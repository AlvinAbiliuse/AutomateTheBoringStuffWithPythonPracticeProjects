from PIL import Image
import os

def resize(image, size):
	editIm = Image.open(os.path.join('Images', image))
	w, h = editIm.size
	print(f'{w} {h}')
	if w >= h:
		if w > size:
			ow = w
			w = size
			ratio = h / ow 
			h = int(w * ratio)
	elif h > w:
		if h > size:
			oh = h
			h = size
			ratio = w / oh 
			w = int(h * ratio)
	print(f'    {w} {h}')
	resizedImage = editIm.resize((w, h))
#	resizedImage.save(f'./Resized/{image}')
	return addLogo(resizedImage, w, h, image)
	

def addLogo(image, width, height, name):
	image.paste(logoIm, ((width - wi), (height - he)), 
                                            logoIm)
	image.save(f'./Resized/{name}')

originalLogoIm = Image.open('catlogo.png')
wi, he = originalLogoIm.size
logoIm = originalLogoIm.resize((int(wi / 8), int(he / 8)))
wi, he = logoIm.size

for i in os.listdir('./Images'):
	mainImage = resize(i, 300)
