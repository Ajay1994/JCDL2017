from collections import defaultdict
import operator
import json
import cPickle as pickle
import matplotlib.pyplot as plt
import numpy
from scipy import stats

prev=set()

# with open("24S_PC_analysis.txt","r") as in_file:
# 	for line in in_file:
# 		try:
# 			entry=line[:-1].split("\t")
# 			prev.add(entry[0])
# 		except KeyError,e:
# 			continue

# with open('13A_maxpaperAuthorCitationCount.json', 'r') as fp2:
#     paperAuthorPC = json.load(fp2)
with open('paperCiter.json', 'r') as fp2:
    paperCiter = json.load(fp2)
for paper in paperCiter:
	prev.add(paper)

newSet=set()
with open("interested_papers.txt","r") as in_file:
	for line in in_file:
		try:
			entry=line.split("\t")
			newSet.add(entry[0])
		except KeyError, e:
			continue

res=set()
res=prev.intersection(newSet)
print len(res)