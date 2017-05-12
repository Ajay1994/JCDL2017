from collections import defaultdict
import operator
import json
import cPickle as pickle
import matplotlib.pyplot as plt
import numpy
from scipy import stats

################## Citation Count Dictionary ###################
with open('10S_paperCitationCount_15years.json', 'r') as fp1:
    paperCitationCount = json.load(fp1)
#########################Check#################################
def corr(x,y):
	r_row, p_value = stats.pearsonr(x, y)
	return r_row

list_t10_5=[]
max_p5=[]

avgDist={}
with open('ccAvgD.txt','r') as f:
	for line in f:
		entry=line[:-1].split("\t")
		avgDist[entry[0]]=entry[1]

op=open("31_PC_CC_results.txt","a")
with open("24S_PC_analysis.txt","r") as in_file:
	for line in in_file:
		try:
			entry=line[:-1].split("\t")
			# print entry
			# if len(entry)<2 or entry[1]=="":
			# 	continue
			if paperCitationCount.has_key(entry[0]) and avgDist.has_key(entry[0]) and float(avgDist[entry[0]])>=2:# and float(avgDist[entry[0]])<2:

				year=paperCitationCount[entry[0]]
				l=year.keys()
				l.sort()
				count=paperCitationCount[entry[0]][l[2]] 
				count1 = paperCitationCount[entry[0]][l[15]]
				# print entry[1]
				if float(entry[1])>=float(28):# and float(entry[1])<float(28):
					list_t10_5.append(count1)
					max_p5.append(float(entry[1]))
		except KeyError,e:
			continue
				# 
# op.write("Correlation Values for pc+ca and citaion count after 15 years\nca:>=2\n0-28\n")
op.write("\n(cc>=28)\n\n")

op.write("All\t")
op.write(str(len(max_p5)))
op.write("\t")
op.write(str(round(corr(max_p5,list_t10_5),3)))
op.write("\n")


