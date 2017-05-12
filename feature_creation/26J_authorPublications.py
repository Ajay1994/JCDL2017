from collections import defaultdict
import operator
import json
import cPickle as pickle

authorPublications=defaultdict(list)

##################paperAuthor dictionary###################
with open('paperAuthor.json', 'r') as fp3:
    paperAuthor = json.load(fp3)


###########################################################
c=0
for publication in paperAuthor:
	for author in paperAuthor[publication]:
		authorPublications[author].append(publication)
	# c+=1
	# if(c==5):
	# 	break
	# print authorPublications

############ dump to json ################################
# with open('26J_authorPublications.json', 'w') as fp5:
#     json.dump(authorPublications, fp5)