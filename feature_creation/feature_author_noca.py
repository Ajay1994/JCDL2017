# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 13:57:02 2016

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

fout = open("./data_files/co_author_graph.txt")
author_noca = dict()
for line in fout:
    author1 = int(line.strip("\n").split("\t")[0])
    author2 = int(line.strip("\n").split("\t")[1])
    if author1 not in author_noca:
        author_noca[author1] = set()
        author_noca[author1].add(author2)
    else:
        author_noca[author1].add(author2)
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


fout = open("./data_files/feature_author_noca.txt", "w")
for paper in paper_authors:
    authors = paper_authors[paper]
    noca = 0
    count = 0
    for author in authors:
        if author in author_noca:
            noca += len(author_noca[author])
            count += 1
    if count == 0:
        count = 1
    fout.write(str(paper) + "\t" + str(float(noca)/count) + "\n")
fout.close()



