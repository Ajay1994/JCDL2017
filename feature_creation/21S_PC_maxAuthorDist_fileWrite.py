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


# paperAuthorPC_CD=defaultdict(dict)

################## Citation Count Dictionary ###################
with open('26J_paperCitationCount_10years.json', 'r') as fp1:
    paperCitationCount = json.load(fp1)

################## Citing Author Publication Count Dictionary ###################
with open('13A_maxEachCiterAuthorPC.json', 'r') as fp2:
    paperAuthorPC = json.load(fp2)

##################paperAuthor dictionary###################
with open('paperAuthor.json', 'r') as fp3:
    paperAuthor = json.load(fp3)

op=open('21S_PC_maxAuthorDist.txt','w')
count=0
for paper in paperCitationCount:
	if paperAuthorPC.has_key(paper):
		# print "new",paper,"::",paperAuthor[paper],"->"
		for author in paperAuthorPC[paper]:
			
			try:
				c=0
				# print len(paperAuthor[paper])
				for a in paperAuthor[paper]:
					# print int(a),int(author),a,paper
					# print a,author
					c+=1
					x=GetShortPath(G1,int(a),int(author))
					if(c==1):
						d=x
					elif(d>x):
						d=x
					# print d,paperAuthorPC[paper][author]
					#print d
				# paperAuthorPC_CD[paper][author]=d
				op.write(str(paper))
				op.write("\t")
				op.write(str(author))
				op.write("\t")
				op.write(str(d))
				op.write("\n")
				# count+=1
				# if count==5:
				# 	print "count is ",count
				# 	break
			except KeyError:
				continue
			except IndexError:
				continue
	# count+=1
	# if count==5:
	# 	break
op.close()		
########### dump to json ################################
# with open('20S_PC_maxAuthorDist.json', 'w') as fp5:
#     json.dump(paperAuthorPC_CD, fp5)	
			
