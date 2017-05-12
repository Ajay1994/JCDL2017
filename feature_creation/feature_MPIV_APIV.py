# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 16:30:57 2016

@author: 15IT60R19
"""

import random
import sys
import os
os.chdir("/home/other/15IT60R19/CitationPrediction")
import numpy as np
from scipy.stats.stats import spearmanr, pearsonr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
import pandas as pd
from matplotlib import style
style.use("ggplot")
from sklearn import svm, preprocessing
from sklearn.svm import SVC
from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import SVR

#Get the list of interested papers
fout = open("./data_files/interested_papers.txt","r")
year_dict = dict()
for line in fout:
    line_list = line.split("\t")
    year_dict[int(line_list[0])] = int(line_list[1])
fout.close()


#cretae the reference dictionary
fin = open("./data_files/citation_network.txt")
citation_dict = dict()
count = 0
for line in fin:
    try:
        list_line = line.strip("\n").split("\t")
        citer = int(list_line[0])
        cited = int(list_line[1])
        if cited not in year_dict or citer not in year_dict:
            continue
        year = int(year_dict[citer])
        if cited == 2:
            print(citer)
            print(year)
        if cited not in citation_dict:
            citation_dict[cited] = dict()
            for i in list(range(1970, 2011)):
                citation_dict[cited][i] = 0
            citation_dict[cited][year] += 1
        else:
            citation_dict[cited][year] += 1
            
        
    except:
        count += 1
fin.close()
    
print("Citation Network Created ...")

for paper in citation_dict:
    total = 0
    for year in citation_dict[paper]:
        total += citation_dict[paper][year]
        citation_dict[paper][year] = total
        
        
fout = open("./data_files/all_papers_venue.txt")
paper_venue = dict()
for line in fout:
    paperid = int(line.strip("\n").split("\t")[0])
    venue = line.strip("\n").split("\t")[1]
    paper_venue[paperid] = venue
fout.close()

############################33

fout = open("./data_files/all_papers_venue.txt")
venue_papers = dict()
for line in fout:
    paperid = int(line.strip("\n").split("\t")[0])
    venue = line.strip("\n").split("\t")[1]
    if venue not in venue_papers:
        venue_papers[venue] = []
        venue_papers[venue].append(paperid)
    else:
        venue_papers[venue].append(paperid)
fout.close()

venue_max_dict = dict()
venue_avg_dict = dict()
for venue in venue_papers:
    papers = venue_papers[venue]
    citations = []
    for paper in papers:
        if paper not in citation_dict:
            continue
        citations.append(citation_dict[paper][2010])
    if len(citations) == 0:
        venue_max_dict[venue] = 0
        venue_avg_dict[venue] = 0
        continue
    venue_max_dict[venue] = max(citations)
    venue_avg_dict[venue] = sum(citations)/len(citations)
    
fout = open("./data_files/feature_venue_MIPA.txt", "w")
for paper in year_dict:
    try:
        fout.write(str(paper) + "\t" + str(venue_max_dict[paper_venue[paper]]) + "\n")
    except:
        continue
fout.close()

fout = open("./data_files/feature_venue_AIPA.txt", "w")
for paper in year_dict:
    try:
        fout.write(str(paper) + "\t" + str(venue_avg_dict[paper_venue[paper]]) + "\n")
    except:
        continue
fout.close()