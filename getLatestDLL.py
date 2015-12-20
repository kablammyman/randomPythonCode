'''
this is a script to grab the latest version of my dll files. Right now, the dll themselves are not versioned
so, the name is misleading...but myabe they will be in the future! This will grab the specified file from the myLibs folder
you can get these 6 versions of my dll
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
import subprocess

DEBUG = 1
RELEASE = 2
DEBUG_X64 = 4
RELEASE_X64 = 8
DEBUG_2010 = 16
RELEASE_2010 = 32

	
def copyFileToDest(file,dest):
	
	if not os.path.exists(os.path.dirname(dest)):
		os.makedirs(os.path.dirname(dest))
		
	if os.path.exists(os.path.dirname(dest)+"\\"+file):
		os.remove(os.path.dirname(dest)+"\\"+file)

	shutil.copyfile(file,dest)
	
def stringToBuildTypeValue(str):
	if str.upper() == "DEBUG":
		return DEBUG
	elif str.upper() == "RELEASE":
		return RELEASE
	elif str.upper() == "DEBUG_X64":
		return DEBUG_X64
	elif str.upper() == "RELEASE_X64":
		return RELEASE_X64
	elif str.upper() == "DEBUG_2010":
		return DEBUG_2010
	elif str.upper() == "RELEASE_2010":
		return RELEASE_2010
	else:
		return -1;
		
def showInvalidBuildTypeMessage():
	print "invalid build type!"
	print "choose between: "
	print "DEBUG"
	print "RELEASE" 
	print "DEBUG_X64" 
	print "RELEASE_X64" 
	print "DEBUG_2010" 
	print "RELEASE_2010"

def showInvlaidParamMessage():
	print "invalid parameters"
	print "your options are:"
	print "-f specify the dll you want (required)"
	print "-d specify where you want to copy the to (if left out, will copy to wher this is ran"
	print "-t specify what build tyoe you (if left out, you get debug version)"
	
def getDllPath(pathBase, type):
	targetPath = pathBase+"\\bin"
	if type == DEBUG:
		targetPath += "\\debug"
	elif type == RELEASE:
		targetPath += "\\release"
	elif type == DEBUG_X64:
		targetPath += "\\debug\\x64"	
	elif type == RELEASE_X64:
		targetPath += "\\release\\x64"	
	elif type == DEBUG_2010:
		targetPath += "\\debug\\vis studio 2010"	
	elif type == RELEASE_2010:
		targetPath += "\\release\\vis studio 2010"	
		
	return targetPath

	
dllName = ""
dllType = DEBUG
pathRoot = "C:\\myLibs" 
destPathRoot = os.path.dirname(os.path.realpath(__file__))

test = False
if test:
	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)
#if we provided our own params, use those instead
if(len(sys.argv) > 2):
	for argIndex, val in enumerate(sys.argv):
		if test:
			print str(argIndex) +" " +str(val)
		if val == "-f":
			dllName = sys.argv[argIndex+1]
			if test:
				print "got the file name: "+ dllName
			
		if val == "-d":
			destPathRoot = sys.argv[argIndex+1]
			if test:
				print "got the destination: "+ destPathRoot
		
		if val == "-t":
			dllType = stringToBuildTypeValue(sys.argv[argIndex+1])
			if dllType == -1:
				showInvalidBuildTypeMessage()
				exit(-1)
			if test:
				print "got the build type: "+ str(dllType)
			
if test:
	print "pathRoot: " + pathRoot
	print "destPathRoot: " + destPathRoot
	print "dllName: " + dllName
	print "dllType: " + str(dllType)
	
if len(destPathRoot) < 3 or not dllName or dllType < 1:
	showInvlaidParamMessage()
	exit(-1)

	
file = getDllPath(pathRoot, dllType)
file += "\\"+dllName
destPathRoot += "\\"+dllName

if test:
	print "file to get: " + file

copyFileToDest(file,destPathRoot)

