# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:41:41 2016

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



tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
p_stemmer = PorterStemmer()

file = "./data/LDA_vocabulary.txt"
##get all texts for training on lda model
texts = []
with open(file, 'r') as myfile:
    raw = myfile.read().replace('\n', '')
    print("file read completed ...")
    tokens = tokenizer.tokenize(raw)
    tokens = [token.lower() for token in tokens]
    stopped_tokens = [i for i in tokens if not i in en_stop]
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    texts.append(stemmed_tokens)
    print("Raw Text prepared ...")
    
dictionary = corpora.Dictionary(texts)
print("Dictionary completed  ...")
with open('./data/LDA_dictionary.pkl', 'wb') as f:
   pickle.dump(dictionary, f)
print("Dictionary Written ...")

"""
pkl_file = open('./data/LDA_dictionary.pkl', 'rb')
dictionary = pickle.load(pkl_file)
pkl_file.close()
"""
print("LDA Model Loading ...")
pkl_file = open('./data/topicmodel_papers.pkl', 'rb')
ldamodel = pickle.load(pkl_file)
pkl_file.close()

print("Model in memory ...")

def findTopic(sentence, dictionary):
    words = tokenizer.tokenize(sentence)
    words = [word.lower() for word in words]
    filteredSentence = [w for w in words if not w in en_stop] 
    filteredSentence = [p_stemmer.stem(i) for i in filteredSentence]
    vec_bow = dictionary.doc2bow(filteredSentence)
    distribution = ldamodel[vec_bow]
    sentVector = np.zeros(100)
    for dist in distribution:
        sentVector[dist[0] - 1] = dist[1]
    return '\t'.join(str(e) for e in sentVector)


print("Topic Modelling Started  ...")
fin = open ("./data/paperid_title_abstract.txt")
fout = open("./data/topic_distribution.txt", "w")
for line in fin:
    line = line.strip("\n").split("\t\t")
    paper_id = line[0]
    paper_title = line[1].strip(".")
    if len(line) > 2:
        paper_abstract = line[2]
    else:
        paper_abstract = ""
    vocabulary = paper_title + " " + paper_abstract
    prob = findTopic(vocabulary, dictionary)
    fout.write(paper_id + " : " + prob + "\n")
fin.close()
fout.close()