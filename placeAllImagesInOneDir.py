# !/usr/bin/python

import os, sys
import shutil

	
srcPath = "C:\\newHaar\\sortedFaces"
desPath = "C:\\newHaar\\faces"

counter = 0;
for path, dirs, files in os.walk(srcPath):
	
	for f in files:		
		oldFile = (path+"\\"+f)
		newFile = desPath+"\\"+str(counter)+".jpg"
		counter += 1
		
		try:
			shutil.copy(oldFile,newFile)
		except:
			print "couldnt copy: "+ source + "\n to: " + destGallery
			#e = sys.exc_info()[0]
			#print e