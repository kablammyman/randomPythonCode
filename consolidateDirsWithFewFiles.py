import os
import sys

path = raw_input( "Enter a file path: ")
fo = open("consolidatedFiles.txt", "w")
print("processing...")

#path, dirs, files = os.walk(path).next()
for path, dirs, files in os.walk(path):
	count = len(files)
	if(count < 5 and len(dirs) == 0):
		index = path.rfind('\\')
		newPath = path[0:index]
		
		for file in files:
			oldFile = path+"\\"+file
			newFile = newPath +"\\"+file
			if(newFile != oldFile and os.path.exists(newFile) == False):
				os.rename(oldFile,newFile )
				fo.write (path + " : " + str(count) + "\n")
		try:
			os.rmdir(path)
		except:
			fo.write ("couldnt move file " + oldFile + "\nto\n" + newFile +"\n")
print("done!")
fo.close()	