from collections import defaultdict
import operator
import json
import cPickle as pickle
import matplotlib.pyplot as plt
import numpy
from scipy import stats

cnt1=0
cnt2=0
cnt=0
with open("21S_PC_maxAuthorDist.txt","r") as in_file:
	for line in in_file:
		entry=line[:-1].split("\t")
		if len(entry)==3:
			if int(entry[2])==0:
				cnt1+=1
			if int(entry[2])==1:
				cnt2+=1
			else:
				cnt+=1
				continue

print cnt			
print cnt1
print cnt2



