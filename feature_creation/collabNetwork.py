from collections import defaultdict
import json;
import cPickle as pickle

collab_one_paper=[]
id_author=defaultdict(set)

# op=open("collaboration_network","wb");
with open("pickup","rb") as infile:
	
	for line in infile:
		try:
			if "#@" in line:
				entry=line[:-1].split(",")
				sz=len(entry)
				for i in range(sz-1):	
					element=entry[i][2:-1].split("[")
					collab_one_paper.append(element[1])
				size=len(collab_one_paper)
				for i in range(size):
					for j in range(size):
						if i==j:
							continue
						else:
							id_author[collab_one_paper[i]].add(collab_one_paper[j])
				del collab_one_paper[:]
		except IndexError:
			continue
# for key in id_author:
# 	op.write(str(key))
# 	op.write(":")
# 	for items in id_author[key]:
# 		op.write(str(items))
# 		op.write(",")
# 	op.write("\n")
# op.close()

# with open('collaboration_network.json', 'w') as fp:
#     json.dump(id_author, fp)
with open('collab.p', 'wb') as fp:
    pickle.dump(id_author, fp)

