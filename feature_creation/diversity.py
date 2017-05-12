# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 17:14:58 2016

@author: 15IT60R19
"""

import os
os.chdir("/home/other/15IT60R19/MTP2/")
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
import pickle
from gensim import corpora, models
import gensim
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np
from scipy import spatial
import math
from scipy import linalg as la
import pandas as pd

fin = open ("./data/topic_distribution.txt")
fout = open("./data/feature_diversity.txt", "w")
count = 0
for line in fin:
    try:
        line = line.strip("\n")
        paper_id = line.split(" : ")[0]
        prob_dist = line.split(" : ")[1].strip("\n")
        prob_dist = prob_dist.split("\t")
        diversity = 0
        for div in prob_dist:
            if div == "0.0":
                continue
            diversity += (-1 * float(div) * math.log(float(div)))
        fout.write(paper_id + "\t" + str(diversity) + "\n")
    except:
        count += 1
        continue
fin.close()
fout.close()