# !/usr/bin/python
#move an image that was saved in its own folder to its proper gallery
import os, sys
import shutil

file = open('dirFix.txt', 'r')

for line in file:
	curPath = line.rstrip('\n')
	print curPath
	os.chdir(curPath)

	for dirpath, dirnames, filenames in os.walk("."):
		for filename in [f for f in filenames if f.endswith(".jpg")]:
			source = os.path.join(dirpath, filename)
			destination = os.getcwd()
			#print "spurce: "+ source + "\ndest: " + destination
			shutil.move(source,destination)

	allDirs = os.walk('.').next()[1]
	for dir in allDirs:
		#print "remove: " + dir
		shutil.rmtree(dir)
