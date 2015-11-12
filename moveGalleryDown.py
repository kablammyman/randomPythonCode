# !/usr/bin/python
#move an image that was saved in its own folder to its proper gallery...this only works for galleries that 
#we know the model's name
import os, sys
import shutil

fileName = 'dirFix.txt'
file = open(fileName, 'r')
lines = file.readlines()
file.close()


file = open(fileName, 'w')

for line in lines:
	curPath = line.rstrip('\n')
	#print curPath

	modelsIndex = curPath.rfind("models")
	starsIndex = curPath.rfind("porn stars")
	amIndex = curPath.rfind("amatuer models")
	
	if modelsIndex == -1 and starsIndex == -1 and amIndex == -1:
		file.write(curPath+"\n")
		continue
	
	
	if modelsIndex == -1:
		modelsIndex = starsIndex;
	if modelsIndex == -1:
		modelsIndex = amIndex;
		
	modelNameIndex = curPath.find("\\", modelsIndex + 2)
	galleryNameIndex = curPath.find("\\", modelNameIndex + 2)
	endOfString = curPath.find("\\", galleryNameIndex + 2)
	
	destGallery = curPath[0:endOfString]
	galDel = curPath.find("\\", endOfString + 2)
	delGallery = curPath[0:galDel]
	
	#print destGallery
	
	moved = False
	for path, dirs, files in os.walk(curPath):
		
		for f in files:
			curFile = (curPath+"\\"+f)
			source = os.path.join(curPath, curFile)
			
			#print "spurce: "+ source + "\ndest: " + destination
			try:
				shutil.move(source,destGallery)
				moved = True
			except:
				print "couldnt move: "+ source + "\n to: " + destGallery
				#e = sys.exc_info()[0]
				#print e

	if moved:
		print "remove: " + delGallery
		shutil.rmtree(delGallery)		
file.close()