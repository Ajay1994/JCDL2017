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


op1=open("1.txt","w")
op2=open("2.txt","w")
op3=open("3.txt","w")
op4=open("4.txt","w")

def w(op,l,paper):
	op.write(str(paper))
	op.write("\t")
	op.write(str(mean(l)))
	# op.write("\t")
	# op.write(str(median(l)))
	# op.write("\t")
	# op.write(str(max(l)))
	# op.write("\t")
	# op.write(str(min(l)))
	op.write("\n")
count=0
for paper in paperCitationCount:
	l1=[]
	l2=[]
	l3=[]
	l4=[]
	if paperAuthorPC.has_key(paper):
		# print "new",paper,"::",paperAuthor[paper],"->"
		for author in paperAuthorPC[paper]:
			
			try:
				c=0
				for a in paperAuthor[paper]:
					# print int(a),int(author),a,paper
					# print a,author
					c+=1
					if(c==1):
						d=GetShortPath(G1,int(a),int(author))
						break
					
				if(d==0):
					l1.append(paperAuthorPC[paper][author])
				elif(d==1):
					l2.append(paperAuthorPC[paper][author])
				elif(d==2):
					l3.append(paperAuthorPC[paper][author])
				else:
					if(d>2):
						l4.append(paperAuthorPC[paper][author])
			except KeyError:
				continue
			except IndexError:
				continue
			
		# print "\n"
		#print "loop"
		op1.write(str(paper))
		op1.write("\t")
		op1.write(str(mean(l1)))
		w(op2,l2,paper)
		w(op3,l3,paper)
		w(op4,l4,paper)
		count+=1
		if(count==10):
			break
op1.close()
op2.close()
op3.close()
op4.close()
			
