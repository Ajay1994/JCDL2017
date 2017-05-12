# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:53:28 2016

@author: 15IT60R19
"""

import os
os.chdir("/home/other/15IT60R19/CitationPrediction/")
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


fout = open("./data_files/interested_papers.txt","r")
year_dict = dict()
for line in fout:
    line_list = line.split("\t")
    year_dict[int(line_list[0])] = int(line_list[1])
fout.close()


fin = open("./data_files/lda_dataset.txt", "w")
fout = open("./data_files/paper_abstract", "r")
for line in fout:
    line_list = line.split("\t")
    paper_id = int(line_list[0])
    if paper_id in year_dict and year_dict[paper_id] <= 2000:
        fin.write(str(line_list[1]))
fin.close()
fout.close()
        