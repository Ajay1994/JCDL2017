from collections import defaultdict
import operator
import json
import cPickle as pickle

################## Citation Count Dictionary ###################
with open('26J_paperCitationCount_10years.json', 'r') as fp1:
    paperCitationCount = json.load(fp1)

################## Citing Author Publication Count Dictionary ###################
with open('13A_maxpaperAuthorCitationCount.json', 'r') as fp2:
    paperAuthorPC = json.load(fp2)

#################################################################################
def median(l):
	l.sort()
	sz=len(l)
	if sz%2==0:
		return float((l[sz/2]+l[sz/2-1])/2)
	return float(l[sz/2])

def mean(l):
	s=0
	sz=len(l)
	if sz==0:
		return 0
	return float(sum(l)/sz)

###################################################################################

# a=[1,5,3,4,6,2,9]
# print median(a)
# print (mean(a))
# print sum(a)
# print max(a)
# print min(a)

op=open("13_CC_analysisTop20Percent.txt","w")

for paper in paperCitationCount:
	temp=[]
	l=[]
	# ind=0
	if paperAuthorPC.has_key(paper):
		op.write(str(paper))
		op.write("\t")
		for author in paperAuthorPC[paper]:
			temp.append(paperAuthorPC[paper][author])
		temp.sort()
		size=len(temp)
		ind=int(0.8*size)
		while (ind<=size-1):
			l.append(temp[ind])
			ind+=1
		op.write(str(mean(l)))
		op.write("\t")
		op.write(str(median(l)))
		op.write("\t")
		op.write(str(max(l)))
		op.write("\t")
		op.write(str(min(l)))
		op.write("\n")