# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:18:35 2016

@author: Ajay Jaiswal
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
        
        
        
fout = open("./data_files/authors_paper.txt")
paper_authors = dict()
for line in fout:
    paperid = int(line.strip("\n").split("\t")[1])
    author_id = int(line.strip("\n").split("\t")[0])
    if paperid not in paper_authors:
        paper_authors[paperid] = []
        paper_authors[paperid].append(author_id)
    else:
        paper_authors[paperid].append(author_id)
fout.close()


fout = open("./data_files/authors_paper.txt")
author_papers = dict()
for line in fout:
    paperid = int(line.strip("\n").split("\t")[1])
    author_id = int(line.strip("\n").split("\t")[0])
    if author_id not in author_papers:
        author_papers[author_id] = []
        author_papers[author_id].append(paperid)
    else:
        author_papers[author_id].append(paperid)
fout.close()

author_max_dict = dict()
author_avg_dict = dict()
for author in author_papers:
    papers = author_papers[author]
    citations = []
    for paper in papers:
        if paper not in citation_dict:
            continue
        citations.append(citation_dict[paper][2010])
    if len(citations) == 0:
        author_max_dict[author] = 0
        author_avg_dict[author] = 0
        continue
    author_max_dict[author] = max(citations)
    author_avg_dict[author] = sum(citations)/len(citations)
    
fout = open("./data_files/feature_author_MIPA.txt", "w")
for paper in paper_authors:
    authors = paper_authors[paper]
    ranks = []
    for author in authors:
        if author in author_max_dict:
            ranks.append(author_max_dict[author])
        else:
            ranks.append(0)
    rank = max(ranks)
    fout.write(str(paper) + "\t" + str(rank) + "\n")
fout.close()

fout = open("./data_files/feature_author_AIPA.txt", "w")
for paper in paper_authors:
    authors = paper_authors[paper]
    ranks = []
    for author in authors:
        if author in author_max_dict:
            ranks.append(author_avg_dict[author])
        else:
            ranks.append(0)
    rank = max(ranks)
    fout.write(str(paper) + "\t" + str(rank) + "\n")
fout.close()