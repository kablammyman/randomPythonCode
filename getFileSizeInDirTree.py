import os
import sys

def bytesto(bytes, to, bsize=1024):
    """convert bytes to megabytes, etc.
       sample code:
           print('mb= ' + str(bytesto(314575262000000, 'm')))

       sample output: 
           mb= 300002347.946
    """
 
    a = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
    r = float(bytes)
    for i in range(a[to]):
        r = r / bsize
 
 
 
path = raw_input( "Enter a file path: ")
fo = open("smallfiles.txt", "w")
print("processing...")
for path, dirs, files in os.walk(path):
  #print path
  for f in files:
	fileSize = os.path.getsize(path+"\\"+f)
	fileSize/=1024
	if(fileSize < 50 ):
		fo.write (path+"\\"+f + " : " + str(fileSize) + " mb\n")
print("done!")
fo.close()	
	
