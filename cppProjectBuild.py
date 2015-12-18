'''
my build script! I get tired of moving the libs I create all over the place, so this script will build the code and move it for me!
Where apploable, I have 6 (!) differnt build types per project:
Debug win32
Relase win32
Debug x64
Release x64
Debug vis studio 2010 win32
Release vis studio 2010 win32

you need put put C:\Program Files (x86)\MSBuild\14.0\Bin in your path for this to work!
'''
#G:\programming\my tools\CFGReader>msbuild cfgreader.sln /p:Configuration="vis studio 2010 Debug"
#G:\programming\my tools\CFGReader>msbuild cfgreader.sln /p:Configuration="Release" /property:Platform=x64
#G:\programming\my tools\CFGReader>msbuild cfgreader.sln /p:Configuration=Release

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


def isFileType(file,ext):
	if file.endswith(ext):
		return True
	return False
	
def moveFileToDest(file,dest):
	
	if not os.path.exists(os.path.dirname(dest)):
		os.makedirs(os.path.dirname(dest))
		
	if os.path.exists(os.path.dirname(dest)+"\\"+file):
		os.remove(os.path.dirname(dest)+"\\"+file)

	shutil.move(file, dest)
	
def copyFileToDest(file,dest):
	
	if not os.path.exists(os.path.dirname(dest)):
		os.makedirs(os.path.dirname(dest))
		
	if os.path.exists(os.path.dirname(dest)+"\\"+file):
		os.remove(os.path.dirname(dest)+"\\"+file)

	shutil.copyfile(file,dest)
	
def moveBuildFiles(binPath,destPathBase,buildType):

	targetPath = ""
	
	if buildType == DEBUG:
		targetPath += "\\debug"
	elif buildType == RELEASE:
		targetPath += "\\release"
	elif buildType == DEBUG_X64:
		targetPath += "\\debug\\x64"	
	elif buildType == RELEASE_X64:
		targetPath += "\\release\\x64"	
	elif buildType == DEBUG_2010:
		targetPath += "\\debug\\vis studio 2010"	
	elif buildType == RELEASE_2010:
		targetPath += "\\release\\vis studio 2010"		
		
	allFiles = os.listdir(binPath)

	for file in allFiles:
		fileName = "\\"+file
		#if not file == baseName
		if isFileType(file,".dll") or isFileType(file,".pdb"):
			destPath = destPathBase + "\\bin" + targetPath
			moveFileToDest(binPath+fileName,destPath+fileName)
		
		elif isFileType(file,".lib"):
			destPath = destPathBase + "\\libs" + targetPath
			moveFileToDest(binPath+fileName,destPath+fileName)

def moveHeaderFile(root, name, dest):
	for root, dirs, files in os.walk(root):
		for f in files:
			if f == name+".h":
				copyFileToDest(root+"\\"+f,dest+"\\"+f)
				return

pathRoot = os.path.dirname(os.path.realpath(__file__))
destPathRoot = "C:\\myLibs"

test = False
if test:
	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)
#if we provided our own params, use those instead
if(len(sys.argv) > 2):
	pathRoot = sys.argv[1]
	destPathRoot = sys.argv[2]

#lets find the sln file. it will also be the name of the exes we build
slnName = ""
baseName = ""
for file in os.listdir(pathRoot):
    if file.endswith(".sln"):
		slnName = file
		baseName = file.split(".")[0]
		break

if test:
	print "pathRoot: " + pathRoot
	print "destPathRoot: " + destPathRoot
	print "slnName: " + slnName
	print "baseName: " + baseName

		
#lets build all the things!
baseBuildCommand = "msbuild \""+ pathRoot + "\\" + slnName + "\" " 

DebugBuild32 = baseBuildCommand + "/p:Configuration=Debug"
ReleaseBuild32 = baseBuildCommand + "/p:Configuration=Release"
DebugBuildx64 = baseBuildCommand + "/p:Configuration=Debug /property:Platform=x64"
ReleaseBuildx64 = baseBuildCommand + "/p:Configuration=Release /property:Platform=x64"

DebugBuild2010 = baseBuildCommand + "/p:Configuration=Debug /p:Configuration=\"vis studio 2010 Debug\""
ReleaseBuild2010 = baseBuildCommand + "/p:Configuration=Release /p:Configuration=\"vis studio 2010 Release\""

moveHeaderFile(pathRoot, baseName, destPathRoot+"\\includes")

if test:
	print buildCommand
print"\nBuilding Debug win32\n"
ret = subprocess.call(DebugBuild32)
if ret == 0:
	binPath = pathRoot + "\\Debug"
	moveBuildFiles(binPath,destPathRoot,DEBUG)

print"\nBuilding Release win32\n"
ret = subprocess.call(ReleaseBuild32)
if ret == 0:
	binPath = pathRoot + "\\Release"
	moveBuildFiles(binPath,destPathRoot,RELEASE)
	
print"\nBuilding Debug x64\n"
ret = subprocess.call(DebugBuildx64)
if ret == 0:
	binPath = pathRoot + "\\x64\\Debug"
	moveBuildFiles(binPath,destPathRoot,DEBUG_X64)

print"\nBuilding Release x64\n"
ret = subprocess.call(ReleaseBuildx64)
if ret == 0:
	binPath = pathRoot + "\\x64\\Release"
	moveBuildFiles(binPath,destPathRoot,RELEASE_X64)

print"\nBuilding Debug v2010\n"
ret = subprocess.call(DebugBuild2010)
if ret == 0:
	binPath = pathRoot + "\\vis studio 2010 Debug"
	moveBuildFiles(binPath,destPathRoot,DEBUG_2010)
	
print"\nBuilding Release 2010\n"
ret = subprocess.call(ReleaseBuild2010)
if ret == 0:
	binPath = pathRoot + "\\vis studio 2010 Release"
	moveBuildFiles(binPath,destPathRoot,RELEASE_2010)
	
print "DONE WITH ALL BUILDS!!"
