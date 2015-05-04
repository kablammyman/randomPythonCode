# !/usr/bin/python
#move images that are saved in its own folder to its proper gallery
import os, sys
import shutil

fileName = 'addGalleryName.txt'
file = open(fileName, 'r')
lines = file.readlines()
file.close()

file = open(fileName, 'w')

index = 0;
galleryName = "generated"
for line in lines:
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
				file.write(curPath+"\n")

	index+=1
file.close()	