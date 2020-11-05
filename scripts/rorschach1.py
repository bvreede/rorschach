from PIL import Image, ImageDraw
import math
import random

question = "File number start"
print question
a = raw_input()
a = int(a)
question = "File number end"
print question
b = raw_input()
b = int(b)
question = "circle or square?"
print question
shape = raw_input()

def square(x,y,length):
	sq1 = x,y
	sq2 = x + length, y
	sq3 = x + length, y + length
	sq4 = x, y + length
	return (sq1,sq2,sq3,sq4)

def rorschach(it):
	width = 5000
	length = 2500
	serpentine = Image.new('RGB', (width, length), 'black')
	DRAW = ImageDraw.Draw(serpentine)
	it = str(it)

	red = 100
	green = 100
	blue = 100
	rad = 5
	ran_x = width/2 - rad
	ran_y = length/2 - rad

	for i in range(0,5000000):
		red = red + random.randint(-2,2)
		#define red variable
		if red >= 255:
			red = 255
		elif red <= 0:
			red = 0
		#define green variable
		green = green + random.randint(-2,2)
		if green >= 255:
			green = 255
		elif green <= 0:
			green = 0
		#define blue variable
		blue = blue + random.randint(-3,2)
		if blue >= 255:
			blue = 255
		elif blue <= 0:
			blue = 0
		#define size of object
		rad = rad # + random.randint(-5,5)
		if rad >= 300:
			rad = 300
		elif rad <= 0:
			rad = 0
		#define x location
		ran_x = ran_x + random.randint(-5,5)
		if ran_x+rad >= width:
			ran_x = width-rad
		elif ran_x <= 0:
			ran_x = 0
		#define y location
		ran_y = ran_y + random.randint(-5,5)
		if ran_y+rad >= length:
			ran_y = length-rad
		elif ran_y <= 0:
			ran_y = 0
		
		if shape == "square":
			#for a square, you need the following line
			DRAW.polygon(square(ran_x,ran_y,rad), fill =(red,green,blue))
		elif shape == "circle":
			#for a circle, you need the following two lines
			circle = (ran_x, ran_y, ran_x+rad, ran_y+rad)
			DRAW.pieslice(circle, 0, 360, fill =(red,green,blue))
		
	name = "rorschach/rorschach_"+ it +".png"
	serpentine.save(name)

for it in range(a,b):
	rorschach(it)




