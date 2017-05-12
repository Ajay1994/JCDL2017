# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 22:29:00 2016

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


#get author citation count till 2000 
fout = open("./data_files/authors_paper.txt")
author_citations = dict()
for line in fout:
    try:
        paperid = int(line.strip("\n").split("\t")[1])
        author_id = int(line.strip("\n").split("\t")[0])
        if author_id not in author_citations:
            author_citations[author_id] = []
            author_citations[author_id].append(citation_dict[paperid][2000])
        else:
            author_citations[paperid].append(citation_dict[paperid][2000])
    except:
        continue
fout.close()

author_avg_citation = dict()
for author in author_citations:
    if len(author_citations[author]) == 0:
        author_citations[author].append(0)
    author_avg_citation[author] = sum(author_citations[author]) / len(author_citations[author])
    
fin = open("./data_files/feature_paper_authorrank.txt", "w")
for paper in year_dict:
    if paper not in paper_authors:
        fin.write(str(paper) + "\t" + "0")
        continue
    paper_author = paper_authors[paper]
    count = 0
    total = 0
    for author in paper_author:
        if author not in author_avg_citation:
            continue
        total += author_avg_citation[author]
        count += 1
    fin.write(str(paper) + "\t" + str(float(total)/count))
    fin.write("\n")
fin.close()


