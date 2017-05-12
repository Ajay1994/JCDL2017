from collections import defaultdict
import operator
import json
import cPickle as pickle
import matplotlib.pyplot as plt
import numpy
from scipy import stats

# prev=set()
def mean(l):
	s=0
	sz=len(l)
	if sz==0:
		return 0
	return float(sum(l))/float(sz)

l1=[]
l2=[]
# with open('26J_authorPublications.json', 'r') as fp3:
#     authorPublications = json.load(fp3)

# for key in authorPublications:
# 	l1.append(len(authorPublications[key]))

with open('11D_authorCiter.json', 'r') as fp3:
    authorCitations = json.load(fp3)

for key in authorCitations:
	l2.append(len(authorCitations[key]))
# with open("24S_PC_analysis.txt","r") as in_file:
# 	for line in in_file:
# 		try:
# 			entry=line[:-1].split("\t")
# 			l1.append(float(entry[1]))
# 		except KeyError,e:
# 			continue

# with open("24S_CC_analysis.txt","r") as in_file:
# 	for line in in_file:
# 		try:
# 			entry=line[:-1].split("\t")
# 			l2.append(float(entry[1]))
# 		except KeyError,e:
# 			continue

print mean(l2)
# print mean(l2)