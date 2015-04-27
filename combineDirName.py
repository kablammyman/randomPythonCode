# !/usr/bin/python
#move images that are saved in its own folder to its proper gallery
import os, sys
import shutil

fileName = 'combineDirName.txt'
file = open(fileName, 'r')
lines = file.readlines()
file.close()

file = open(fileName, 'w')

for line in lines:
	curPath = line.rstrip('\n')
	#print curPath
	
	lastDirIndex = curPath.rfind("\\",0, len(curPath)-2)
	lastFolderName = curPath[lastDirIndex+1:len(curPath)]
	
	secondDirIndex =  curPath.rfind("\\",0, lastDirIndex)
	secondFolderName = curPath[secondDirIndex+1:lastDirIndex]
	
	newPath = curPath[0:secondDirIndex+1]
	#print "1st folder: " + lastFolderName + " index " + str(lastDirIndex) 
	#print "2nd folder: " + secondFolderName + " index " + str(secondDirIndex)
	
	newFolderName = secondFolderName+lastFolderName
	
	
	delGallery = curPath[0:lastDirIndex+1]
	
	
	newDir = newPath+newFolderName
	
	if not os.path.exists(newDir):
		os.makedirs(newDir)
	
	print newDir

	for path, dirs, files in os.walk(curPath):
		for f in files:
			fileImg = curPath+"\\"+f
			try:
				shutil.move(fileImg,newDir)
				delList.append(delGallery)
			except:
				print "couldnt move: " + fileImg + "\nto\n"+newDir 
				file.write(curPath+"\n")
file.close()

#now delete empty dirs	
for delDir in delList:  
	if os.path.exists(delDir):
		shutil.rmtree(delDir)	

	
