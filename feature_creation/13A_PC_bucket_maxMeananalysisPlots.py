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
	plt.scatter(x4,y4,c='k',label='20-100')
	plt.scatter(x3,y3,c='y',label='10-20',color='yellow')
	plt.scatter(x2,y2,c='g',label='5-10',color='green')
	plt.scatter(x1,y1,c='b',label='0-5',color='blue')
	plt.legend(loc='upper left')
	plt.xlabel('max of publication counts of citers in 2 years')
	plt.ylabel('cummulative Citation count after 10 years')
	# plt.xscale('log')
	# plt.yscale('log')
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

with open("13_PC_analysis.txt","r") as in_file:
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
				max_p1.append(float(entry[1]))
			elif count>=int(5) and count<int(10):
				list_t10_2.append(count1)
				max_p2.append(float(entry[1]))
			elif count>=int(10) and count<int(20):
				list_t10_3.append(count1)
				max_p3.append(float(entry[1]))
			elif count>=int(20) and count<int(100):
				list_t10_4.append(count1)
				max_p4.append(float(entry[1]))
			# elif count>=int(100) and count<int(1000):
			# 	list_t10_5.append(count1)
			# 	max_p5.append(int(entry[3]))
			else:
				if count>=int(100): 
					list_t10_6.append(count1)
					max_p6.append(float(entry[1]))
				


# print max_p1[0],list_t10_1[0]
# print len(max_p1),len(list_t10_1)
# plot(max_p1,list_t10_1,"cummulative Citation count(0-4) after 10 years")
#plot(max_p2,list_t10_2,"cummulative Citation count(4-10) after 10 years")
#plot(max_p3,list_t10_3,"cummulative Citation count(>=10) after 10 years")
# t=preprocess(max_p1,list_t10_1)
# print t
plot1(max_p1,max_p2,max_p3,max_p4,max_p6, list_t10_1,list_t10_2,list_t10_3,list_t10_4,list_t10_6)


