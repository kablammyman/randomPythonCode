# !/usr/bin/python
#move an image that was saved in its own folder to its proper gallery...this only works for galleries that have no known name
import os, sys
import shutil

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

usingSubwebsite = False;

if str(sys.argv[0]) == "true" or len(sys.argv) > 1:
	print "using subswebsite"
	usingSubwebsite = True
else:
	print "gerneic site"

fileName = 'moveUnkownGallery.txt'
file = open(fileName, 'r')
lines = file.readlines()
file.close()
delList = []

file = open(fileName, 'w')
pathRoot = "\\\\OPTIPLEX-745\\photos\\porno pics"
for line in lines:
	curPath = line.rstrip('\n')
	#print curPath

	modelsIndex = curPath.rfind("models")
	starsIndex = curPath.rfind("porn stars")
	amIndex = curPath.rfind("amatuer models")
	
	if modelsIndex != -1 or starsIndex != -1 or amIndex != -1:
		file.write(curPath+"\n")
		continue
	
	
	shortenedPath = curPath.replace(pathRoot,"")	
	#print shortenedPath
	
	numLoops = 3
	if usingSubwebsite:
		numLoops = 4;
	lastSlash = 1

	for x in range(0, numLoops):
		lastSlash = shortenedPath.find("\\",lastSlash) + 1

		
	destGallery = pathRoot+shortenedPath[0:lastSlash]
	print destGallery

	galDel = curPath.find("\\", len(destGallery)+1)
	delGallery = curPath[0:galDel]
	
	#print delGallery
	
	for path, dirs, files in os.walk(curPath):
		
		for f in files:
			curFile = (curPath+"\\"+f)
			source = os.path.join(curPath, curFile)
			
			#print "source: "+ source + "\ndest: " + destination
			try:
				if os.path.isfile(destGallery+"\\"+f):
					delList.append(delGallery)
					continue
				shutil.move(source,destGallery)
				delList.append(delGallery)
			except IOError, e:
				print "Unable to copy file. %s" % e
				file.write(curPath+"\n")
				pass
file.close()

#now delete empty dirs	
for delDir in delList:  
	if os.path.exists(delDir):
		shutil.rmtree(delDir)	