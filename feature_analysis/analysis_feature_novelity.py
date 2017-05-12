# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 16:36:14 2016

@author: 15IT60R19
"""
import os
os.chdir("/home/other/15IT60R19/CitationPrediction")
import numpy as np
from scipy.stats.stats import spearmanr, pearsonr
import pandas as pd
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


fin = open("./data_files/cummulative_citation_profile.txt")
total_citation = dict()
for line in fin:
    list_line = line.strip("\n").split("\t")
    profile = list_line[2].split(",")
    total_citation[int(list_line[0])] = int(profile[len(profile) - 2])
fin.close()

fin = open("./data_files/feature_paper_novality.txt")
paper_novality = dict()
for line in fin:
    try:
        paper_id = int(line.strip("\n").split("\t")[0])
        novality = float(line.strip("\n").split("\t")[1])
        paper_novality[paper_id] = round(novality, 2)
    except:
        continue
fin.close()

nov_dict = dict()
total = 0
for paper in paper_novality:
    nov = paper_novality[paper]
    if paper not in total_citation:
        continue
    else:
        citation = total_citation[paper]
    total += citation
    if nov not in nov_dict:
        nov_dict[nov] = []
        nov_dict[nov].append(citation)
    else:
        nov_dict[nov].append(citation)
        
novality = []
citation_count = []
for nov in nov_dict:
    novality.append(nov)
    x = sum(nov_dict[nov])
    citation_count.append(x/len(nov_dict[nov]))
    
plt.scatter(novality, citation_count)
plt.show()
