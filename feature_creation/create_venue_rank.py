# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 13:33:12 2016

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


fout = open("./data/paperid_venue.txt")
venue_papers = dict()
for line in fout:
    try:
        paperid = int(line.strip("\n").split("\t")[0])
        venue = line.strip("\n").split("\t")[1]
        #if paper_year[paperid] > 2009:
        if paper_year[paperid] > 2009 and paper_year[paperid] < 2005:
            continue
        if venue not in venue_papers:
            venue_papers[venue] = []
            venue_papers[venue].append(paper_citation[paperid])
        else:
            venue_papers[venue].append(paper_citation[paperid])
    except:
        continue
fout.close()


venue_expected_citation = dict()
for venue in venue_papers:
    venue_expected_citation[venue] = (sum(venue_papers[venue]) * 1.0)/len(venue_papers[venue])
    
venue_id = []
citations = []
for venue in venue_expected_citation:
    citations.append(venue_expected_citation[venue])
    venue_id.append(venue)


venue_rank = pd.Series(citations, index = venue_id)
venue_rank.sort(ascending = False)
rank = venue_rank.index


count = 1
fout = open("./data/venue_rank_recent.txt", "w")
for item in rank:
    fout.write(str(item) + "\t" + str(count) + "\n")
    count += 1
fout.close()

