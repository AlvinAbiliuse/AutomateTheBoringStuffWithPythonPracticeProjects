from PIL import Image, ImageDraw

im = Image.new('RGBA', (360 * 2, 288 * 2), 'white')
draw = ImageDraw.Draw(im)
draw.text((50, 50), 'Welcome Master Anikin', fill='black')
flowerIm = Image.open('img.png').convert('RGBA')
resizedFlowerIm = flowerIm.resize((260 * 2, 188 * 2))
im.paste(resizedFlowerIm, (50 * 2, 50 * 2), resizedFlowerIm)
im.save('flowerImTextLarger.png')
