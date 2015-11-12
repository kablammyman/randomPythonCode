import os
import sys

path = raw_input( "Enter a file path: ")
goodList = open("nameFaceCsv.txt", "w")
badList = open("notEnoughImagesList.txt", "w")

print("processing...")

#path, dirs, files = os.walk(path).next()
for path, dirs, files in os.walk(path):
	#get model name from path
	index = path.rfind('\\')
	modelName = path[index+1:]
	#if we hve less than X num of files, put in bad list so we can go and fix that later
	count = len(files)
	if(count < 10):
		badList.write (path + "\n")
	else:	
		for filename in files:
			csvLine = modelName +","+ os.path.join(path, filename)
			goodList.write (csvLine + "\n")

print("done!")
goodList.close()	
badList.close()	