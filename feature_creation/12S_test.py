from collections import defaultdict
import operator
import json
import cPickle as pickle

from snap import *

G1=TUNGraph.New()

with open("nodes.txt","r") as node:
	for line in node:
		G1.AddNode(int(line[:-1]))

with open("edges.txt","r") as edge:
	for line in edge:
		entry=line[:-1].split("\t")
		G1.AddEdge(int(entry[0]),int(entry[1]))

################## Citation Count Dictionary ###################
with open('26J_paperCitationCount_10years.json', 'r') as fp1:
    paperCitationCount = json.load(fp1)

################## Citing Author Publication Count Dictionary ###################
with open('13A_maxEachCiterAuthorPC.json', 'r') as fp2:
    paperAuthorPC = json.load(fp2)

##################paperAuthor dictionary###################
with open('paperAuthor.json', 'r') as fp3:
    paperAuthor = json.load(fp3)

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


# op1=open("12S_PC_analysis1.txt","w")
# op2=open("12S_PC_analysis2.txt","w")
# op3=open("12S_PC_analysis3.txt","w")
# op4=open("12S_PC_analysis4.txt","w")

# def w(op,l):
# 	op.write(str(paper))
# 	op.write("\t")
# 	op.write(str(mean(l)))
# 	# op.write("\t")
# 	# op.write(str(median(l)))
# 	# op.write("\t")
# 	# op.write(str(max(l)))
# 	# op.write("\t")
# 	# op.write(str(min(l)))
# 	op.write("\n")

for paper in paperCitationCount:
	l1=[]
	l2=[]
	l3=[]
	l4=[]
	if paperAuthorPC.has_key(paper):
		for author in paperAuthorPC[paper]:
			d=10000000
			try:
				for a in paperAuthor[paper]:
					# print int(a),int(author),a,paper
					if(d>GetShortPath(G1,int(a),int(author))):
						d=GetShortPath(G1,int(a),int(author))
			except KeyError:
				continue
			except IndexError:
				continue
			print d
			if(d==0):
				l1.append(paperAuthorPC[paper][author])
			elif(d==1):
				l2.append(paperAuthorPC[paper][author])
			elif(d==2):
				l3.append(paperAuthorPC[paper][author])
			else:
				if(d>2):
					l4.append(paperAuthorPC[paper][author])

			w(op1,l1)
			w(op2,l2)
			w(op3,l3)
			w(op4,l4)