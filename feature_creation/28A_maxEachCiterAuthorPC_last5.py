from collections import defaultdict
import operator
import json
import cPickle as pickle



paperAuthorPC=defaultdict(dict)



################## authorPublications dictionary ###################
with open('26J_authorPublications.json', 'r') as fp3:
    authorPublications = json.load(fp3)


##################paperAuthor dictionary###################
with open('paperAuthor.json', 'r') as fp1:
    paperAuthor = json.load(fp1)


###################### Paper year #############################
paperYear={}
with open("paper_years_final","rb") as infile:
	for line in infile:
		entry=line[:-1].split("\t")
		paperYear[entry[0]]=int(entry[1])



####################calculate union of authors#####################
# def calculateAuthors(all_papers_in_2_years,paperAuthor):
# 	authors=set()
# 	for paper in all_papers_in_2_years:
# 		if paperAuthor.has_key(paper):
# 			for author in paperAuthor[paper]:
# 				authors.add(author)
# 	return authors



################## Calculation of Publication count(till y+2) of all authors citing the paper in 2 years of its publication ###############
def calculateAuthorPC(a,authorPublications,paperYear,year):
	pc=0
	if authorPublications.has_key(a):
		for publication in authorPublications[a]:
			if paperYear.has_key(publication):
				if paperYear[publication]<=year+2:
					pc+=1
	return pc


###########################################################

c=0
with open("paperCiterFinal","rb") as pc:
	for line in pc:
		
		yearPaper=defaultdict(set)
		all_papers_in_2_years=set()

		entry=line[:-1].split(":")
		if paperYear.has_key(entry[0]):
			try:
				# yearPaper[paperYear[entry[0]]].add(entry[0])
				paper=entry[0]
				year=paperYear[paper]
				# print paper," ",year,"\n"
			except KeyError:
				continue
			except IndexError:
				continue
		else:
			continue
		element=entry[1].split(",")
		sz=len(element)
		
		for i in range(sz):
			try:
				if paperYear[element[i]]<=year+2 and paperYear[element[i]]>=year-3:
					if paperAuthor.has_key(element[i]):
						m=0
						for a in paperAuthor[element[i]]:
							a_pc=calculateAuthorPC(a,authorPublications,paperYear,year)
							# print a,a_pc
							if a_pc>m:
								m=a_pc
								key=a
						paperAuthorPC[paper][key]=m
					# print paperAuthorPC
					# break

		
			except KeyError:
				continue
			except IndexError:
				continue
		# break

		# authors=calculateAuthors(all_papers_in_2_years,paperAuthor)
		# # print authors,"\n"
		
		# if len(authors)>0:
		# 	paperAuthorPC[paper]=calculateAuthorPC(authors,authorPublications,paperYear,year)
		# c+=1
		# if(c==5):
		# 	break

############ dump to json ################################
with open('28A_maxEachCiterAuthorPC_last5.json', 'w') as fp5:
    json.dump(paperAuthorPC, fp5)