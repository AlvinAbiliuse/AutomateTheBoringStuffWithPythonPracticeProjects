#!/usr/bin/env python3

import os
from PIL import Image

def imageSearch(files, folder):
	n = 0
	if len(files) == 0:
		return
	else:
		for i in files:
			if i.endswith(('jpg', 'jpeg', 'bmp', 'png')):
				im = Image.open(folder + '/' + i)
				w, h = im.size
				if w < 500:
					continue
				elif h < 500:
					continue 
				n += 1
		if n >= (len(files) / 2):
			print(f'{folder} is a photos folder')


for dirname, subdirname, filename in os.walk(input('Insert Absolute Path:\n')):
	# print(dirname)
	# print(filename, end='\n\n')
	imageSearch(filename, dirname)
