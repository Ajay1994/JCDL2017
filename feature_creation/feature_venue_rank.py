# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 15:42:25 2016

@author: 15IT60R19
"""
import os
os.chdir("/home/other/15IT60R19/CitationPrediction")
import numpy as np
from scipy.stats.stats import spearmanr, pearsonr
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd
from matplotlib import style
style.use("ggplot")
from sklearn import svm, preprocessing
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
import pickle
from gensim import corpora, models
import gensim
from nltk.tokenize import sent_tokenize, word_tokenize
from scipy import spatial
import math
from scipy import linalg as la
import pandas as pd

#Get the list of interested papers
fout = open("./data_files/interested_papers.txt","r")
year_dict = dict()
for line in fout:
    line_list = line.split("\t")
    year_dict[int(line_list[0])] = int(line_list[1])
fout.close()

fout = open("./data_files/all_papers_venue.txt")
paper_venue = dict()
for line in fout:
    paperid = int(line.strip("\n").split("\t")[0])
    venue = line.strip("\n").split("\t")[1]
    paper_venue[paperid] = venue
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
        
        
#get venue citation count till 2000 
fout = open("./data_files/all_papers_venue.txt")
venue_citations = dict()
for line in fout:
    try:
        paperid = int(line.strip("\n").split("\t")[0])
        venue = line.strip("\n").split("\t")[1]
        if venue not in venue_citations:
            venue_citations[venue] = []
            venue_citations[venue].append(citation_dict[paperid][2000])
        else:
            venue_citations[venue].append(citation_dict[paperid][2000])
    except:
        continue
fout.close()

venue_avg_citation = dict()
for venue in venue_citations:
    if len(venue_citations[venue]) == 0:
        venue_citations[venue].append(0)
    venue_avg_citation[venue] = float(sum(venue_citations[venue])) / len(venue_citations[venue])
    
fin = open("./data_files/feature_paper_venuerank.txt", "w")
for paper in year_dict:
    try:
        fin.write(str(paper) + "\t" + str(venue_avg_citation[paper_venue[paper]]))
        fin.write("\n")
    except:
        continue
fin.close()