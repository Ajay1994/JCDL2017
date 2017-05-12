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

list_t10=[]

mean=[]
median=[]
max_p=[]
min_p=[]

op=open("29J_PC_Correlation.txt","w")

with open("27J_analysis.txt","r") as in_file:
	for line in in_file:
		entry=line[:-1].split("\t");
		# print entry

		if paperCitationCount.has_key(entry[0]):

			year=paperCitationCount[entry[0]]
			# print paperCitationCount[entry[0]][max(year)]
			list_t10.append(paperCitationCount[entry[0]][max(year)])
			mean.append(float(entry[1]))
			median.append(float(entry[2]))
			max_p.append(int(entry[3]))
			min_p.append(int(entry[4]))

# print len(mean) ,len(list_t10)
# print mean
op.write("Mean and Publication Count after 10 years\t")
op.write(str(pc(mean,list_t10)))
op.write("\n")
op.write("Median and Publication Count after 10 years\t")
op.write(str(pc(median,list_t10)))
op.write("\n")
op.write("Max and Publication Count after 10 years\t")
op.write(str(pc(max_p,list_t10)))
op.write("\n")
op.write("Min and Publication Count after 10 years\t")
op.write(str(pc(min_p,list_t10)))
op.write("\n")
