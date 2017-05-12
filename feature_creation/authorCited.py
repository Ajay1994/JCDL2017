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
with open('paperAuthor.json', 'r') as fp:
    paperAuthor = json.load(fp)

paperCited=defaultdict(set)
with open("citation_network_new","rb") as infile2:
	for line in infile2:
		entry=line[:-1].split('\t')
		paperCited[entry[0]].add(entry[1])
		
#creating dictionary author cited**************************
AuthorCited=defaultdict(list)
for key in paperAuthor:
	for author in paperAuthor[key]:
		# print("inside authors loop")
		if len(paperCited[key])>0:
			for items in paperCited[key]:
				AuthorCited[author].append(items)
print AuthorCited

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
