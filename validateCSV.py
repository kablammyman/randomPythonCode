import os
import sys

fileName = 'csv.txt'
file = open(fileName, 'r')
lines = file.readlines()
file.close()


dict = {}
modelList = []

for line in lines:
	splitString = line.split(',');
	curPath = splitString[1].rstrip('\n')
		
	if os.path.exists(curPath) and not (line in dict):
		dict[line] = True
		modelList.append( line );
		
modelList.sort()

file = open(fileName, 'w')

for entry in modelList:
	file.write(entry)	

file.close()