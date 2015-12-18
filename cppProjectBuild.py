'''
my build script! I get tired of moving the libs I create all over the place, so this script will build the code and move it for me!
Where apploable, I have 6 (!) differnt build types per project:
Debug win32
Relase win32
Debug x64
Release x64
Debug vis studio 2010 win32
Release vis studio 2010 win32
'''


# !/usr/bin/python
import os, sys
import shutil

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)


#fileName = "filesToMove"
#file = open(fileName, 'w')

#G:\programming\my tools\CFGReader>msbuild cfgreader.sln /p:Configuration="vis studio 2010 Debug"
#G:\programming\my tools\CFGReader>msbuild cfgreader.sln /p:Configuration="Release" /property:Platform=x64
#G:\programming\my tools\CFGReader>msbuild cfgreader.sln /p:Configuration=Release

pathRoot = "G:\\programming\\my tools\\openCVTest\\Debug\\faceDB"
destPath = "C:\\faces"

print os.path.dirname(os.path.realpath(__file__))
moveFilesOver = False
removeSpacesFromName = True
#path, dirs, files = os.walk(path).next()
path = pathRoot
for path, dirs, files in os.walk(path):
	print "folder name: " + path
	print "num files to move: " + str(len(files))
	
	if removeSpacesFromName:
		for f in files:
			fileName = f.rstrip()
			#print "old: " + str(len(f)) + " new: " + str(len(fileName))
			oldFielName = pathRoot+"\\"+f+"\\"
			newFileName = pathRoot+"\\"+fileName
			print newFileName
			os.rename(oldFielName,newFileName)


	if moveFilesOver:
		for f in files:
			curFile = (pathRoot+"\\"+f)
			#source = os.path.join(curPath, curFile)
			if not os.path.exists(curFile):
				os.makedirs(curFile)
	
exit(0)