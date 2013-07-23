import cv #Import functions from OpenCV
import sys
import os

#combines an image with a grey binary image
def shade(filename):
	filename = str(filename)
	image=cv.LoadImage(filename, cv.CV_LOAD_IMAGE_COLOR)
	cv.ShowImage('image',image)
	binary = cv.CreateImage( cv.GetSize(image),8,1 ); 
	
	#convert original color image (3 channel rgb color image) to gray-level image 
	cv.CvtColor( image, binary, cv.CV_RGB2GRAY )
	
	threshold=100
	colour=255
	
	#uses a binary threshold to convert the gray image
	cv.EqualizeHist(binary,binary)
	cv.Threshold(binary,binary, threshold,colour,cv.CV_THRESH_BINARY)#cv.CV_THRESH_BINARY)
	cv.Threshold(binary,binary, threshold,colour,cv.CV_THRESH_OTSU)
	
	for y in range(0, image.height):
		for x in range(0, image.width):
			pixel= cv.Get2D(binary, y, x) # Slow get pixel value.
			#if( pixel[0]==0 and pixel[1]==0 and pixel[2]==0):
				#cv.Set2D(image, y, x, cv.RGB(0,0,0))#(0, 0, 0, 0))
			if( pixel[0]<50 and pixel[1]<50 and pixel[2]<50):
				cv.Set2D(image, y, x, cv.RGB(pixel[0],pixel[1],pixel[2]))#(0, 0, 0, 0))
			#else:
				#pixels= cv.Get2D(image, y, x)
				#cv.Set2D(image, y, x, cv.RGB(int((3*pixels[2])/4),int((3*pixels[1])/4),int((3*pixels[0])/4)))#(0, 0, 0, 0))
	cv.ShowImage('binary',binary)
	cv.ShowImage('image1',image)
	
	#splits the filename from its extension
	list = os.path.splitext(filename)
	name = list[0] + 'car.png'
	#print name

	cv.SaveImage(name, image)
	cv.SaveImage('binary.png', binary)

#combines an image with the edges detected using the canny algorithm
def edges(filename):
	filename = str(filename)
	image=cv.LoadImage(filename, cv.CV_LOAD_IMAGE_COLOR)
	cv.ShowImage('image',image)
	canny = cv.CreateImage( cv.GetSize(image),8,1 ); 
	
	#convert original color image (3 channel rgb color image) to gray-level image 
	cv.CvtColor( image, canny, cv.CV_RGB2GRAY )
	
	cv.Canny( canny, canny, 10, 100, 3 )
				
	for y in range(0, image.height):
		for x in range(0, image.width):
			pixel= cv.Get2D(canny, y, x) # Slow get pixel value.
			pixels= cv.Get2D(image, y, x)
			#inverse colors
			#if( pixel[0]==0 and pixel[1]==0 and pixel[2]==0):
				#cv.Set2D(image, y, x, cv.RGB(0,0,0))#(0, 0, 0, 0))
			if( pixel[0]==0 and pixel[1]==0 and pixel[2]==0):
				cv.Set2D(image, y, x, cv.RGB(pixels[2],pixels[1],pixels[0]))#(0, 0, 0, 0))
			else:
				cv.Set2D(image, y, x, cv.RGB(0,0,0))#(0, 0, 0, 0))

	cv.ShowImage('canny',canny)
	cv.ShowImage('image2',image)
	
	#splits the filename from its extension
	list = os.path.splitext(filename)
	name = list[0] + 'can.png'
	#print name

	cv.SaveImage(name, image)
	cv.SaveImage('canny.png', canny)
	

#combines an image with the edges detected using the canny algorithm 
#after smoothing the image
def edgesSmooth(filename):
	filename = str(filename)
	image=cv.LoadImage(filename, cv.CV_LOAD_IMAGE_COLOR)
	cv.ShowImage('image',image)
	canny = cv.CreateImage( cv.GetSize(image),8,1 ); 
	
	#convert original color image (3 channel rgb color image) to gray-level image 
	cv.CvtColor( image, canny, cv.CV_RGB2GRAY )
	
	cv.Smooth(canny,canny,cv.CV_MEDIAN)
	cv.Canny( canny, canny, 10, 100, 3 )
	
	for y in range(0, image.height):
		for x in range(0, image.width):
			pixel= cv.Get2D(canny, y, x) # Slow get pixel value.
			pixels= cv.Get2D(image, y, x)
			if( pixel[0]==0 and pixel[1]==0 and pixel[2]==0):
				cv.Set2D(image, y, x, cv.RGB(pixels[2],pixels[1],pixels[0]))#(0, 0, 0, 0))
			else:
				cv.Set2D(image, y, x, cv.RGB(0,0,0))#(0, 0, 0, 0))

	cv.ShowImage('canny',canny)
	cv.ShowImage('image3',image)
	
	#splits the filename from its extension
	list = os.path.splitext(filename)
	name = list[0] + 'canSm.png'
	#print name

	cv.SaveImage(name, image)
	cv.SaveImage('cannySm.png', canny)


def main(arg):
	#print sys.argv
	if len(arg)<2:
		raw_input('add filename')
	
	
	else:
		filename = arg[1]
		print filename

		shade(filename)
		#edges(filename)
		#edgesSmooth(filename)
		
		#pauses so that the open images can be viewed
		cv.WaitKey(10000)

if __name__== "__main__":
	main(sys.argv)

