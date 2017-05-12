# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 19:15:24 2016

@author: 15IT60R19
"""

import random
import sys
import os
os.chdir("/home/other/15IT60R19/CitationPrediction")
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
import pandas as pd
from matplotlib import style
style.use("ggplot")
from sklearn import svm, preprocessing
from sklearn.svm import SVC
from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import SVR
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
import pickle
import numpy as np
from scipy import spatial
import math
from scipy import linalg as la
import pandas as pd

tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
p_stemmer = PorterStemmer()


pkl_file = open('./data/LDA_dictionary.pkl', 'rb')
dictionary = pickle.load(pkl_file)
pkl_file.close()

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
fin = open ("./data_files/paperid_title_abstract.txt")
fout = open("./data_files/topic_distribution.txt", "w")
for line in fin:
    line = line.strip("\n").split("\t\t")
    paper_id = line[0]
    paper_title = line[1].strip(".")
    paper_abstract = line[2]
    vocabulary = paper_title + " " +paper_abstract
    prob = findTopic(vocabulary, dictionary)
    fout.write(paper_id + " : " + prob + "\n")
fin.close()
fout.close()

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