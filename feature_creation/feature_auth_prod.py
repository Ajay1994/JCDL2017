# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:48:51 2016

@author: Ajay Jaiswal
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


fout = open("./data_files/feature_author_productivity.txt", "w")
max_prod = 0
for paper in year_dict:
    authors = paper_authors[paper]
    prod = 0
    for author in authors:
        productivity = set()
        papers = author_papers[author]
        for p in papers:
            if p in year_dict and year_dict[p] <= year_dict[paper]:
                productivity.add(p)
        prod += len(productivity)
    prod = prod/len(authors)
    fout.write(str(paper) + "\t" + str(prod) + "\n")
fout.close()
