# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:18:28 2016

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

## for tokenizing , and removing stopwords
tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
p_stemmer = PorterStemmer()

fout = open("./data_files/lda_dataset.txt")
##get all texts for training on lda model
vocab_data = dict()
# loop through document list
for doc in fout:
    # clean and tokenize document string
    raw = doc.lower()
    tokens = tokenizer.tokenize(raw)
    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    # stem tokens
    stemmed_tokens = [i for i in stemmed_tokens if len(i) > 2]   
    
    # add tokens to vocabulary dictionary
    for word in stemmed_tokens:
        if word not in vocab_data:
            vocab_data[word] = 1
        else:
            vocab_data[word] += 1
fout.close()

with open('./data_files/vocabulary.pickle', 'wb') as handle:
  pickle.dump(vocab_data, handle)

"""
with open('./data_files/vocabulary.pickle', 'rb') as handle:
  vocab_data = pickle.load(handle)
"""

print("writng vocabulary to text file")
fout = open("./data_files/vocabulary.txt", "w")
for word in vocab_data:
    if vocab_data[word] <= 5:
        continue
    else:
        fout.write(word + "\t" + str(vocab_data[word]) + "\n")
fout.close()