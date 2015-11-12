'''
this code is to help recover some face images since windows goofed, and i have to move files by hand! >:(
the "files" are really directories that wondows cant seem to find, so i used them to create new dirs somewhere else
and I had to move the files by hand >:(

edit, turns out the problem was that theres a space at the end of the folder name, whhich is illegal in windows!
so i renamed the folders to not have the space, to make this woirkm i had to add teh trailling slash, otherwise
windows itself would have a fit.
'''


# !/usr/bin/python
#move an image that was saved in its own folder to its proper gallery...this only works for galleries that have no known name
import os, sys
import shutil

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)


#fileName = "filesToMove"
#file = open(fileName, 'w')

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