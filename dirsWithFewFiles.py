import os
import sys

path = raw_input( "Enter a file path: ")
#minNumFiles = raw_input( "Enter a the minimum amount of files a folder needs: ")
fo = open("fewFiles.txt", "w")
print("processing...")

#path, dirs, files = os.walk(path).next()
for path, dirs, files in os.walk(path):
	count = len(files)
	if(count < 5 and len(dirs) == 0):
		fo.write (path + " : " + str(count) + "\n")
print("done!")
fo.close()	