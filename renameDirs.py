# !/usr/bin/python

import os, sys

# listing directories
#print "The dir is: %s"%os.listdir(os.getcwd())
allDirs = os.listdir(os.getcwd())

for s in allDirs:
	oldString = str(s)
	newString = oldString.replace("-", " ")
	try:
		os.rename(oldString,newString)
	except WindowsError:
		print "old: " + oldString
		print "new: " + newString
		print  sys.exc_info()[0]

print "Successfully renamed."
