from collections import defaultdict
from io import open
import json

count=0
#loop=0
op = open("id_author_hash","wb")
id_author=defaultdict(set)
with open("pickup","rb") as infile:
	
	for line in infile:
		try:
			if "#@" in line:
				entry=line[:-1].split(",")
				
				for i in range(len(entry)-1):	
					element=entry[i][2:-1].split("[")
					id_author[element[1]].add(element[0])
					
		except IndexError:
			continue

for key in id_author:
	op.write(str(key))
	op.write(":")
	for items in id_author[key]:
		op.write(str(items))
		op.write(",")
	op.write("\n")
op.close()

	
