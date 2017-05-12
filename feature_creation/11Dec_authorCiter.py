from collections import defaultdict
import operator
import json
import cPickle as pickle
import matplotlib.pyplot as plt
import numpy
from scipy import stats


################## paperCiter dictionary ###################
with open('paperCiter.json', 'r') as fp2:
    paperCiter = json.load(fp2)


##################paperAuthor dictionary###################
with open('paperAuthor.json', 'r') as fp1:
    paperAuthor = json.load(fp1)


authorCiter=defaultdict(list)

for paper in paperAuthor:
	for a in paperAuthor[paper]:
		try:
			for c in paperCiter[paper]:
				try:
					authorCiter[a].append(c)
				except KeyError,e:
					continue
		except KeyError,e:
				continue

with open('11D_authorCiter.json', 'w') as fp5:
	json.dump(authorCiter, fp5)