from collections import defaultdict
import json;
import cPickle as pickle

collab_one_paper=[]
id_author=defaultdict(list)

op=open("paperCiterFinal","wb");
with open("citation_network_new","rb") as infile:
	
	for line in infile:
		
		entry=line[:-1].split("\t")
		if len(entry)==2:
			id_author[entry[1]].append(entry[0])

# count=0				
# for key in id_author:
# 	print(key)
# 	count+=1
# 	if key<>"":
# 		op.write(str(key))
# 		op.write(":")
# 		for items in id_author[key]:
# 			op.write(str(items))
# 			op.write(",")
# 		op.write("\n")
# 	# if count==2:
# 	# 	break
# op.close()
with open('paperCiter.json', 'w') as fp:
    json.dump(id_author, fp)

# with open('data.p', 'wb') as fp:
#     pickle.dump(id_author, fp)

