from collections import defaultdict
import operator
import json
import cPickle as pickle
import matplotlib.pyplot as plt
import numpy
# from scipy import stats
################# Citation Count Dictionary ###################
with open('26J_paperCitationCount_10years.json', 'r') as fp1:
    paperCitationCount = json.load(fp1)


################################################################
def plot(x,y,s):
	plt.plot(x, y,'ro')
	plt.ylabel('cummulative Citation count after 10 years')
	plt.xlabel(s)
	plt.show()

# def pc(x,y):
# 	return stats.pearsonr(x, y)

list_t10=[]
##################################################################

op=open("1A_CC_Correlation.txt","w")

mean=[]
median=[]
max_p=[]
min_p=[]
with open("1A_CitationCountAnalysis.txt","r") as in_file:
	for line in in_file:
		entry=line[:-1].split("\t")
		# print entry

		if paperCitationCount.has_key(entry[0]):

			year=paperCitationCount[entry[0]]
			# print paperCitationCount[entry[0]][max(year)]
			list_t10.append(paperCitationCount[entry[0]][max(year)])
			mean.append(float(entry[1]))
			median.append(float(entry[2]))
			max_p.append(int(entry[3]))
			min_p.append(int(entry[4]))

plot(mean,list_t10,"mean of Citation counts of citers in 2 years")
plot(median,list_t10,"median of Citation counts of citers in 2 years")
plot(max_p,list_t10,"max of Citation counts of citers in 2 years")
plot(min_p,list_t10,"min of Citation counts of citers in 2 years")

