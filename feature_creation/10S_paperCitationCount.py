from collections import defaultdict
import operator
import json
import cPickle as pickle

paperCitationCount=defaultdict(dict)

###################### Paper year #############################
paperYear={}
with open("paper_years_final","rb") as infile:
	for line in infile:
		entry=line[:-1].split("\t")
		paperYear[entry[0]]=int(entry[1])

################## Calculation of citation count list ###############
def calculateCitations(paper,year,yearPaper):
	l={}
	if yearPaper.has_key(year):				 # taking same year citation count 
		# print yearPaper[year]
		l[year]=(len(yearPaper[year]))
	else:
		l[year]=0

	# print year,"\n"
	year+=1 								# increment year to check in subsequent years

	for i in range(15):
		l[year]=l[year-1]
		if yearPaper.has_key(year):
			l[year]=l[year]+len(yearPaper[year])
		year+=1

	# print yearPaper,"\n&&&&&&&&&\n",l
	return l

###############################################################
c=0
with open("paperCiterFinal","rb") as pc:
	for line in pc:
		
		yearPaper=defaultdict(set)
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
				yearPaper[paperYear[element[i]]].add(element[i])
		
			except KeyError:
				continue
			except IndexError:
				continue
		paperCitationCount[paper]=calculateCitations(paper,year,yearPaper)
		# c+=1
		# if(c==2):
		# 	break

with open('10S_paperCitationCount_15years.json', 'w') as fp5:
	json.dump(paperCitationCount, fp5)
