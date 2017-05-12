# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:18:28 2016

@author: 15IT60R19
"""

import os
os.chdir("/home/other/15IT60R19/MTP2")
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

## for tokenizing , and removing stopwords
tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
p_stemmer = PorterStemmer()

print("Tokenizer created ...")

#Create the vocabulary set
vocabulary = set()
fin = open("./data_files/vocabulary.txt")
for line in fin:
    word = line.strip("\n").split("\t")[0]
    vocabulary.add(word)
fin.close()

print("Vocabulary Created ...")

#Get the list of interested papers
fout = open("./data_files/interested_papers.txt","r")
year_dict = dict()
for line in fout:
    line_list = line.split("\t")
    year_dict[int(line_list[0])] = int(line_list[1])
fout.close()


#create the term frequency matrix
fin = open("./data_files/paper_abstract")
tf_dict = dict()
for line in fin:
    line = line.strip("\n")
    paper_id = int(line.split("\t")[0])
    paper_abstract = line.split("\t")[1]
    if paper_id not in year_dict:
        continue
    
    raw = paper_abstract.lower()
    tokens = tokenizer.tokenize(raw)
    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    # stem tokens
    stemmed_tokens = [i for i in stemmed_tokens if len(i) > 2]
    
    tf_dict[paper_id] = dict()
    for word in stemmed_tokens:
        if word in vocabulary:
            if word not in tf_dict[paper_id]:
                tf_dict[paper_id][word] = 1
            else:
                tf_dict[paper_id][word] += 1
fin.close()


with open('./data_files/tf_matrix.pickle', 'wb') as handle:
  pickle.dump(tf_dict, handle)


#with open('./data/tf_matrix.pickle', 'rb') as handle:
#  tf_dict = pickle.load(handle)  


print("Term frequency Matrix Created ...")