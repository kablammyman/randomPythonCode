import os
import sys
import shutil

file = open("fewfiles.txt", "r")
print("processing...")

for line in file:
	line = line.split(":", 1)
	path = line[0].split("\n",1)
	cleanPath =  path[0]
	print cleanPath
	shutil.rmtree(cleanPath)
		
print("done!")
file.close()	
	
