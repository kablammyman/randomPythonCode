import os
import sys
from PIL import Image
'''	
pil_im=Image.open("C:\\newHaar\\faces\\C\\Cabby\\2.jpg")
width, height = pil_im.size
print "C:\\newHaar\\faces\\C\\Cabby\\2.jpg" + 

exit(0)
'''
path = raw_input( "Enter a file path: ")
fo = open("allFiles.txt", "w")
print("processing...")

#path, dirs, files = os.walk(path).next()
for path, dirs, files in os.walk(path):
	for file in files:
		fullPath = path + "\\" + file
		pil_im=Image.open(fullPath)
		width, height = pil_im.size
		#first "param is num objs in img (2 spaces between that and rect dims), then x,y, the width and height
		#if more than 1 param, 3 spaces before next x,y, w, h
		fo.write (fullPath + "  1  0 0 "+ str(width) + " " + str(height) + "\n")
print("done!")
fo.close()	