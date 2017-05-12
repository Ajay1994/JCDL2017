from collections import defaultdict
import json;

paperAuthor=defaultdict(list)

op = open("paper_author","wb")
count=0
with open("pickup","rb") as infile:
	for line in infile:
		
		try:
			if "#index" in line:
				# op.write(str(line[6:-1])+'\t')
				key=line[6:-1]
			elif "#@" in line:
					entry=line[:-1].split(",")
					sz=len(entry)
					for i in range(sz-1):	
						element=entry[i][2:-1].split("[")
						# op.write(str(element[1])+',')
						paperAuthor[key].append(element[1])
					# op.write("\n")
			else:
				continue
		except IndexError:
			continue
op.close()

with open('paperAuthor.json', 'w') as fp:
    json.dump(paperAuthor, fp)