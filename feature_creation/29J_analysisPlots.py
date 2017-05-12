from collections import defaultdict
import operator
import json
import cPickle as pickle
import matplotlib.pyplot as plt

################## Citation Count Dictionary ###################
with open('26J_paperCitationCount_10years.json', 'r') as fp1:
    paperCitationCount = json.load(fp1)


################################################################
def plot(x,y,s):
	plt.plot(x, y,'ro')
	plt.ylabel('cummulative Citation count after 10 years')
	plt.xlabel(s)
	plt.show()

list_t10=[]

mean=[]
median=[]
max_p=[]
min_p=[]
with open("27J_analysis.txt","r") as in_file:
	for line in in_file:
		entry=line[:-1].split("\t");
		print entry

		if paperCitationCount.has_key(entry[0]):

			year=paperCitationCount[entry[0]]
			# print paperCitationCount[entry[0]][max(year)]
			list_t10.append(paperCitationCount[entry[0]][max(year)])
			mean.append(entry[1])
			median.append(entry[2])
			max_p.append(entry[3])
			min_p.append(entry[4])


plot(mean,list_t10,"mean of publication counts of citers in 2 years")
plot(median,list_t10,"median of publication counts of citers in 2 years")
plot(max_p,list_t10,"max of publication counts of citers in 2 years")
plot(min_p,list_t10,"max of publication counts of citers in 2 years")

