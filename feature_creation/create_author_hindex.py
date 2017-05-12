# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 20:06:33 2016

@author: 15IT60R19
"""

import os
os.chdir("/home/other/15IT60R19/MTP2")
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

fout = open("./data/paperid_pubyear.txt")
paper_year = dict()
for line in fout:
    try:
        paperid = int(line.strip("\n").split("\t")[0])
        year = int(line.strip("\n").split("\t")[1])
        paper_year[paperid] = year
    except:
        continue
fout.close()


fout = open("./data/paper_citation_profile.txt")
fin = open("./data/paperid_citationcount.txt")
paper_citation = dict()
for line in fin:
    try:
        paper_id = int(line.strip("\n").split("\t")[0])
        citation = int(line.strip("\n").split("\t")[1])
        paper_citation[paper_id] = citation
    except:
        continue
fin.close()

fout = open("./data/paperid_authorid.txt")
author_papers = dict()
for line in fout:
    paperid = int(line.strip("\n").split("\t")[0])
    author_id = int(line.strip("\n").split("\t")[1])
    if paper_year[paperid] > 2009:
        continue
    if author_id not in author_papers:
        author_papers[author_id] = []
        author_papers[author_id].append(paper_citation[paperid])
    else:
        author_papers[author_id].append(paper_citation[paperid])
fout.close()

def gethindex(citations):
    citations = np.sort(citations)
    #print(citations)
    result = 0
    for i in list(range(0, len(citations))):
        small = min(citations[i], len(citations) - i)
        result = max(result, small)
        #print(i, small, result)
    return result

fout = open("./data/author_hindex.txt", "w")
for author in author_papers:
    citations = author_papers[author]
    hindex = gethindex(citations)
    fout.write(str(author) + "\t" + str(hindex)+ "\n")
fout.close()
    