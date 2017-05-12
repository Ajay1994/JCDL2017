from collections import defaultdict
import operator
import json
import cPickle as pickle
import matplotlib.pyplot as plt
import numpy
from scipy import stats

################## Citation Count Dictionary ###################
with open('26J_paperCitationCount_10years.json', 'r') as fp1:
    paperCitationCount = json.load(fp1)


def pc(x,y):
	return stats.pearsonr(x, y)


op=open("9A_CC_Correlation_buckets_more_than_100.txt","w")

list_t10_1=[]
list_t10_2=[]
list_t10_3=[]
list_t10_4=[]
list_t10_5=[]
list_t10_6=[]

max_p1=[]
max_p2=[]
max_p3=[]
max_p4=[]
max_p5=[]
max_p6=[]

with open("1A_CitationCountAnalysis.txt","r") as in_file:
	for line in in_file:
		entry=line[:-1].split("\t");
		# print entry
		if int(entry[3])>100:
			if paperCitationCount.has_key(entry[0]):

				year=paperCitationCount[entry[0]]
				l=year.keys()
				l.sort()
				count=paperCitationCount[entry[0]][l[2]]
				count1 = paperCitationCount[entry[0]][l[-1]]

				if count>=int(0) and count<int(5):	
					list_t10_1.append(count1)
					max_p1.append(int(entry[3]))
				elif count>=int(5) and count<int(10):
					list_t10_2.append(count1)
					max_p2.append(int(entry[3]))
				elif count>=int(10) and count<int(20):
					list_t10_3.append(count1)
					max_p3.append(int(entry[3]))
				elif count>=int(20) and count<int(100):
					list_t10_4.append(count1)
					max_p4.append(int(entry[3]))
				
				else:
					if count>=int(100): 
						list_t10_6.append(count1)
						max_p6.append(int(entry[3]))
				

op.write("for more than 100 CC\n*************************************************************\n\n")
op.write("Max CC and cumulative citation count(0-5) after 10 years\t")
op.write(str(pc(max_p1,list_t10_1)))
op.write("\n")

op.write("Max CC and cumulative citation count(5-10) after 10 years\t")
op.write(str(pc(max_p2,list_t10_2)))
op.write("\n")

op.write("Max CC and cumulative citation count(10-20) after 10 years\t")
op.write(str(pc(max_p3,list_t10_3)))
op.write("\n")

op.write("Max CC and cumulative citation count(20-100) after 10 years\t")
op.write(str(pc(max_p4,list_t10_4)))
op.write("\n")

op.write("Max CC and cumulative citation count(>=100) after 10 years\t")
op.write(str(pc(max_p6,list_t10_6)))
op.write("\n")



