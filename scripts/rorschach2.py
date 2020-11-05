from PIL import Image, ImageDraw
import math, random

numfiles = 40
redmin = 0
redmax = 200
greenmin = 0
greenmax = 150
bluemin = 50
bluemax = 200
colorjump = 1
radmin = 15
radmax = 1500
jump = 750

def square(x,y,length):
	sq1 = x,y
	sq2 = x + length, y
	sq3 = x + length, y + length
	sq4 = x, y + length
	return (sq1,sq2,sq3,sq4)

def drawpic(width,length):
	red = 50
	green = 50
	blue = 50
	opac = 255
	opacmin = 255
	opacmax = 255
	rad = 30
	ranx = width/2 - rad
	rany = length/2 - rad

	for i in range(0,8000):
		red = red + random.randint(-colorjump,colorjump)
		#define red variable
		if red >= redmax:
			red = redmax
		elif red <= redmin:
			red = redmin
		#define green variable
		green = green + random.randint(-colorjump,colorjump)
		if green >= greenmax:
			green = greenmax
		elif green <= greenmin:
			green = greenmin
		#define blue variable
		blue = green + random.randint(-colorjump,colorjump)
		if blue >= bluemax:
			blue = bluemax
		elif blue <= bluemin:
			blue = bluemin
		#define opacity
		opac = 255
	#	if opac >= opacmax:
	#		opac = opacmax
	#	elif opac <= opacmin:
	#		opac = opacmin
	
		#define size of object
		rad = rad + random.randint(-5,5)
		if rad >= radmax:
			rad = radmax
		elif rad <= radmin:
			rad = radmin
		#define x location
		ranx = ranx + random.randint(-jump,jump)
		if ranx+rad >= width:
			ranx = width-rad
		elif ranx <= (0-rad):
			ranx = (0-rad)
		#define y location
		rany = rany + random.randint(-jump,jump)
		if rany+rad >= length:
			rany = length-rad
		elif rany <= (0-rad):
			rany = (0-rad)
	
		#for a square, you need the following line
		#DRAW.polygon(square(ran5,ran6,rad), fill =(red,green,blue))
	
		#for a circle, you need the following two lines
		circle = (ranx, rany, ranx+rad, rany+rad)
		DRAW.pieslice(circle, 0, 360, fill =(red,green,blue,opac))

for i in range(numfiles):
	width = 15000
	length = 15000
	serpentine = Image.new('RGBA', (width, length), 'white')
	DRAW = ImageDraw.Draw(serpentine)
	drawpic(width,length)
	name = "rorschach/rorschach%s.png" %(i)
	serpentine.save(name)
