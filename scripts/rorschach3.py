from PIL import Image, ImageDraw
from images2gif import writeGif
import math, random, csv, os

redmin = 0
redmax = 255
greenmin = 0
greenmax = 255	
bluemin = 0
bluemax = 255
radmin = 10
radmax = 300	
jump = 50
jump2 = 50
colorjump = 5
colorjump2 = 2
radjump = 10
width = 2500
length = 2500
numimg = 200
numdots = 1000
numfolder = 1

def makevar():
	#start values
	red = 50
	green = 50
	blue = 50
	rad = 50
	ranx = width/2 - rad
	rany = length/2 - rad

	for i in range(0,numdots):
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
		blue = blue + random.randint(-colorjump,colorjump)
		if blue >= bluemax:
			blue = bluemax
		elif blue <= bluemin:
			blue = bluemin
		#define size of object
		rad = rad + random.randint(-radjump,radjump)
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
		outputfile.write("%s,%s,%s,%s,%s,%s\n" %(red,green,blue,rad,ranx,rany))
		
def changevar(red,green,blue,rad,ranx,rany):
	red = red + random.randint(-colorjump2,colorjump2)
	#define red variable
	if red >= redmax:
		red = redmax
	elif red <= redmin:
		red = redmin
	#define green variable
	green = green + random.randint(-colorjump2,colorjump2)
	if green >= greenmax:
		green = greenmax
	elif green <= greenmin:
		green = greenmin
	#define blue variable
	blue = blue + random.randint(-colorjump2,colorjump2)
	if blue >= bluemax:
		blue = bluemax
	elif blue <= bluemin:
		blue = bluemin
	#define size of object
	rad = rad + random.randint(-radjump,radjump)
	if rad >= radmax:
		rad = radmax
	elif rad <= radmin:
		rad = radmin
	#define x location
	ranx = ranx + random.randint(-jump2,jump2)
	if ranx+rad >= width:
		ranx = width-rad
	elif ranx <= (0-rad):
		ranx = (0-rad)
	#define y location
	rany = rany + random.randint(-jump2,jump2)
	if rany+rad >= length:
		rany = length-rad
	elif rany <= (0-rad):
		rany = (0-rad)
	outputfile.write("%s,%s,%s,%s,%s,%s\n" %(red,green,blue,rad,ranx,rany))

#Draw Image
def makeimg(inputdb,outdir,seq):
	serpentine = Image.new('RGB', (width, length), 'white')
	DRAW = ImageDraw.Draw(serpentine)
	db = csv.reader(open("%s/%s" %(outdir,inputdb)))
	for line in db:
		circle = (int(line[4]), int(line[5]), int(line[3])+int(line[4]), int(line[3])+int(line[5]))
		DRAW.pieslice(circle, 0, 360, fill =(int(line[0]),int(line[1]),int(line[2])))
	name = "%s/rorschachimage_%s_%s.png" %(outdir,outdir[15:],seq)
	serpentine.save(name)

for i in range(numfolder):
	outdir = "movingrorschach%s" %(i)
	if os.path.exists(outdir):
		print "overwriting %s" %(outdir)
	else:
		os.mkdir(outdir)
	source = "%s/rorschachdb_%s_0.csv" %(outdir,i)
	outputfile = open(source, "w")
	makevar()
	outputfile.close()
	for k in range(1,numimg):
		source = "%s/rorschachdb_%s_%s.csv" %(outdir,i,k-1)
		dest = "%s/rorschachdb_%s_%s.csv" %(outdir,i,k)
		outputfile = open(dest, "w")
		db = csv.reader(open(source))
		for line in db:
			changevar(int(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5]))
		outputfile.close()

	for file in os.listdir(outdir):
		if file[-4:] == ".csv":
			seq = file[14:-4]
			if len(seq) == 1:
				seq = '0'+seq
			makeimg(file,outdir,seq)
			os.remove("%s/%s" %(outdir,file))
	
	file_names = sorted((fn for fn in os.listdir(outdir) if fn.endswith('.png'))) #['animationframa.png', 'animationframb.png', 'animationframc.png', ...] "
	images = [Image.open("%s/%s" %(outdir,fn)) for fn in file_names]
	#images.extend(reversed(images)) #infinit loop will go backwards and forwards.
	filename = "%s/rorschachmovie%s.gif" %(outdir,i)
	writeGif(filename, images, duration=0.1)