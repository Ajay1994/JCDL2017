from collections import defaultdict
import operator
import json
import cPickle as pickle
import matplotlib.pyplot as plt

################## Citation Count Dictionary ###################
with open('26J_paperCitationCount_10years.json', 'r') as fp1:
    paperCitationCount = json.load(fp1)
#########################Check#################################
# for key in paperCitationCount:
# 	print key
# 	year=paperCitationCount[key]
# 	print year
# 	l=year.keys()
# 	l.sort()
# 	print l[2]

# 	print paperCitationCount[key][max(year)]
# 	break
def mean(l):
	s=0
	sz=len(l)
	if sz==0:
		return 0
	return float(sum(l)/sz)

################### Preprocess ###############################
def preprocess(x,y):
	d=defaultdict(list)
	s=len(x)
	for i in range(s):
		d[x[i]].append(y[i])
	t={}
	for i in range(s):
		t[x[i]]=mean(d[x[i]])
	# print len(t.keys()),len(t.values()),"\n"
	return t

###################Plot##############################
# def plot(x,y,s):
# 	plt.scatter(x, y)
# 	plt.xlabel('max of publication counts of citers in 2 years')
# 	plt.ylabel(s)
# 	#plt.xscale('log')
# 	#plt.yscale('log')
# 	plt.show()
def plot1(x1,x2,x3,x4,x6,y1,y2,y3,y4,y6):
	plt.scatter(x6,y6,c='r',label='>=100',color='red')
	# plt.scatter(x5,y5,c='m',label='100-200')
	plt.scatter(x4,y4,c='k',label='20-100',color='black')
	plt.scatter(x3,y3,c='y',label='10-20',color='yellow')
	plt.scatter(x2,y2,c='g',label='5-10',color='green')
	plt.scatter(x1,y1,c='b',label='0-5',color='blue')
	plt.legend(loc='upper left')
	plt.xlabel('max of Citation counts of citers in 2 years')
	plt.ylabel('cummulative Citation count after 10 years')
	# plt.xscale('log')
	# plt.yscale('log')
	plt.show()
def plot2(x1,x2,x3,x4,x6,y1,y2,y3,y4,y6):
	plt.scatter(x6,y6,c='r',label='>=100',color='red')
	# plt.scatter(x5,y5,c='m',label='100-200')
	plt.scatter(x4,y4,c='k',label='20-100',color='black')
	plt.scatter(x3,y3,c='y',label='10-20',color='yellow')
	plt.scatter(x2,y2,c='g',label='5-10',color='green')
	plt.scatter(x1,y1,c='b',label='0-5',color='blue')
	plt.legend(loc='upper left')
	plt.xlabel('max of Citation counts of citers in 2 years')
	plt.ylabel('cummulative Citation count after 10 years')
	plt.xscale('log')
	plt.yscale('log')
	plt.show()

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
			# elif count>=int(100) and count<int(1000):
			# 	list_t10_5.append(count1)
			# 	max_p5.append(int(entry[3]))
			else:
				if count>=int(100): 
					list_t10_6.append(count1)
					max_p6.append(int(entry[3]))
				


t1=preprocess(max_p1,list_t10_1)
t2=preprocess(max_p2,list_t10_2)
t3=preprocess(max_p3,list_t10_3)
t4=preprocess(max_p4,list_t10_4)
t5=preprocess(max_p6,list_t10_6)
# print len(t1.keys()),len(t1.values())
# print len(t2.keys()),len(t2.values())
# print len(t3.keys()),len(t3.values())
# print len(t4.keys()),len(t4.values())
# print len(t5.keys()),len(t5.values())

plot1(t1.keys(),t2.keys(),t3.keys(),t4.keys(),t5.keys(),t1.values(),t2.values(),t3.values(),t4.values(),t5.values())
plot2(t1.keys(),t2.keys(),t3.keys(),t4.keys(),t5.keys(),t1.values(),t2.values(),t3.values(),t4.values(),t5.values())



