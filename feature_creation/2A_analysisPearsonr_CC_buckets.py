from collections import defaultdict
import operator
import json
import cPickle as pickle
import matplotlib.pyplot as plt
import numpy
from scipy import stats
################# Citation Count Dictionary ###################
with open('26J_paperCitationCount_10years.json', 'r') as fp1:
    paperCitationCount = json.load(fp1)


################################################################
# def plot(x,y,s):
# 	plt.plot(x, y,'ro')
# 	plt.ylabel('cummulative Citation count after 10 years')
# 	plt.xlabel(s)
# 	plt.show()

def pc(x,y):
	return stats.pearsonr(x, y)

op=open("2A_CC_Correlation_buckets.txt","w")


##################################################################



list_t10_1=[]
list_t10_2=[]
list_t10_3=[]

max_p1=[]
max_p2=[]
max_p3=[]

with open("1A_CitationCountAnalysis.txt","r") as in_file:
	for line in in_file:
		entry=line[:-1].split("\t");
		# print entry

		if paperCitationCount.has_key(entry[0]):

			year=paperCitationCount[entry[0]]
			count=paperCitationCount[entry[0]][max(year)]
			if count>=float(0) and count<float(4):
				list_t10_1.append(count)
				max_p1.append(float(entry[3]))
			elif count>=float(4) and count<float(10):
				list_t10_2.append(count)
				max_p2.append(float(entry[3]))
			else:
				if count>=float(10):
					list_t10_3.append(count)
					max_p3.append(float(entry[3]))

op.write("Max CC and cumulative citation count(0-4) after 10 years\t")
op.write(str(pc(max_p1,list_t10_1)))
op.write("\n")

op.write("Max CC and cumulative citation count(4-10) after 10 years\t")
op.write(str(pc(max_p2,list_t10_2)))
op.write("\n")

op.write("Max CC and cumulative citation count(>=10) after 10 years\t")
op.write(str(pc(max_p3,list_t10_3)))
op.write("\n")

