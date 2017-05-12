# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:29:17 2016

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


fin = open("./data_files/co_author_graph.txt", "w")
def getCombination(authors):
    for i in list(range(0, len(authors) - 1)):
        for j in list(range(i + 1, len(authors))):
            fin.write(str(authors[i]) + "\t" + str(authors[j]) + "\n")
            fin.write(str(authors[j]) + "\t" + str(authors[i]) + "\n")
            
for paper in paper_authors:
    authors = paper_authors[paper]
    getCombination(authors)

fin.close()