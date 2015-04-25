# !/usr/bin/python
#move an image that was saved in its own folder to its proper gallery
import os, sys
import shutil

file = open('addGalleryName.txt', 'r')
index = 0;
galleryName = "generated"
for line in file:
	curPath = line.rstrip('\n')
	print curPath
	#os.chdir(curPath)

	newGallery =galleryName+str(index)
	newDir = curPath+newGallery
	
	print newDir
	if not os.path.exists(newDir):
		os.makedirs(newDir)

	for path, dirs, files in os.walk(curPath):
		for f in files:
			file = curPath+"\\"+f
			try:
				shutil.move(file,newDir)
			except:
				print "couldnt move: " + file + "\nto\n"+newDir 

	index+=1
	