from collections import defaultdict
import operator
import json
import cPickle as pickle

################## Citation Count Dictionary ###################
with open('26J_paperCitationCount_10years.json', 'r') as fp1:
    paperCitationCount = json.load(fp1)

################## Citing Author Publication Count Dictionary ###################
with open('1A_paperAuthorCitationCount.json', 'r') as fp2:
    paperAuthorCC = json.load(fp2)

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

op=open("1A_CitationCountAnalysis.txt","w")

for paper in paperCitationCount:
	l=[]
	if paperAuthorCC.has_key(paper):
		op.write(str(paper))
		op.write("\t")
		for author in paperAuthorCC[paper]:
			l.append(paperAuthorCC[paper][author])
		op.write(str(mean(l)))
		op.write("\t")
		op.write(str(median(l)))
		op.write("\t")
		op.write(str(max(l)))
		op.write("\t")
		op.write(str(min(l)))
		op.write("\n")