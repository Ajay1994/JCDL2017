# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:22:45 2016

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


## for tokenizing , and removing stopwords
tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
p_stemmer = PorterStemmer()

fout = open("./data_files/lda_dataset.txt")
##get all texts for training on lda model
texts = []
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
    
    # add tokens to list
    texts.append(stemmed_tokens)
fout.close()    
    
# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
print("Dictionary completed  ...")   

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]
print("Corpus Made ...")

# generate LDA model
print("Model trainning ...")
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=100, id2word = dictionary, passes=100)
print("Model Trainned ...")

with open('./data_files/topicmodel_papers.pkl', 'wb') as f:
   pickle.dump(ldamodel, f)
print("Model Written ...")

"""
raw = doc.lower()
tokens = tokenizer.tokenize(raw)
# remove stop words from tokens
stopped_tokens = [i for i in tokens if not i in en_stop]
# stem tokens
stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
# stem tokens
stemmed_tokens = [i for i in stemmed_tokens if len(i) > 2] 
#tokenize the sentence



words = word_tokenize("Modelling Public Administration Portals ")
words = [word.lower() for word in words]


#filter out the words in sentences which not belong to stop word category
filteredSentence = [w for w in words if not w in en_stop] 
#for each word of the sentence create a word2Vec and add each one to form a sentence vector

sentVector = np.zeros(10)
##from lda model get sent vec
vec_bow = dictionary.doc2bow(filteredSentence)
print(ldamodel[vec_bow])

"""