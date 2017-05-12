from collections import defaultdict
import json


#input*******************
# op=open("authorCited","wb")

# paperAuthor=defaultdict(set)
# with open("paper_author","rb") as infile1:
# 	for line in infile1:
# 		entry=line[:-2].split("\t")
# 		authors=entry[1].split(",")
# 		sz=len(authors)
# 		for i in range(sz-1):
# 			paperAuthor[entry[0]].add(authors[i])
with open('AuthorCited.json', 'r') as fp:
    paperAuthor = json.load(fp)

cnt=0

for author in paperAuthor:
	cnt+=1
print cnt

#writing to the output file********************************
# for key in AuthorCited:
# 	op.write(str(key))
# 	op.write(":")
# 	for items in AuthorCited[key]:
# 		op.write(str(items))
# 		op.write(",")
# 	op.write("\n")
# op.close()

# with open('AuthorCited.json', 'w') as fp:
#     json.dump(AuthorCited, fp)
