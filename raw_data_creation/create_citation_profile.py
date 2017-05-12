# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 16:37:28 2016

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

fin = open("./data_files/citation_profile.txt", "w")
profile = dict()
for paper in citation_dict:
    profile = citation_dict[paper]
    fin.write(str(paper) + "\t")
    fin.write(str(year_dict[paper]) + "\t")
    for year in profile:
        fin.write(str(profile[year]) + ",")
    fin.write("\n")
fin.close()
    