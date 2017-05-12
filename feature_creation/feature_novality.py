# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 23:15:07 2016

@author: 15IT60R19
"""

import os
os.chdir("/home/other/15IT60R19/CitationPrediction/")
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

with open('./data_files/tf_matrix.pickle', 'rb') as handle:
  tf_dict = pickle.load(handle)  
  
#Get the list of interested papers
fout = open("./data_files/interested_papers.txt","r")
year_dict = dict()
for line in fout:
    line_list = line.split("\t")
    year_dict[int(line_list[0])] = int(line_list[1])
fout.close()

#Create the vocabulary set
vocabulary = set()
fin = open("./data_files/vocabulary.txt")
for line in fin:
    word = line.strip("\n").split("\t")[0]
    vocabulary.add(word)
fin.close()

print("Vocabulary Created ...")

#cretae the reference dictionary
fin = open("./data_files/citation_network.txt")
reference_dict = dict()
for line in fin:
    try:
        list_line = line.strip("\n").split("\t")
        citer = int(list_line[0])
        cited = int(list_line[1])
        if cited not in year_dict or citer not in year_dict:
            continue
        if citer not in reference_dict:
            reference_dict[citer] = []
            reference_dict[citer].append(cited)
        else:
            reference_dict[citer].append(cited)
    except:
        print(line)
fin.close()
    
print("Citation Network Created ...")

normalization = dict()
for doc in tf_dict:
    denominator = 0.0
    for word in vocabulary:
        if word in tf_dict[doc]:
            denominator += tf_dict[doc][word]
    normalization[doc] = denominator

print("Normalization factor created ...")

with open('./data_files/normalization.pickle', 'wb') as handle:
  pickle.dump(normalization, handle)
  
with open('./data_files/normalization.pickle', 'rb') as handle:
  normalization = pickle.load(handle) 

  
def getProb(doc,word):
    numinator = 0.0
    if word in tf_dict[doc]:
        numinator = tf_dict[doc][word]
    denominator = normalization[doc]
    #print(numinator)
    #print(denominator)
    if denominator <= 0:
        return 0
    return numinator/denominator


# Kullback–Leibler divergence from Q to P, denoted DKL(P‖Q), is a measure of the 
# information gained when one revises one's beliefs from the prior probability 
# distribution Q to the posterior probability distribution P. In other words, it is 
# the amount of information lost when Q is used to approximate P. Kullback–Leibler 
# divergence also measures the expected number of extra bits required to code samples 
# from P using a code optimized for Q rather than the code optimized for P.

def getKLDivergence(doc1, doc2):
    result = 0
    for word in tf_dict[doc1]:
        term1 = getProb(doc1, word)
        term2 = getProb(doc2, word)
        if term1 > 0 and term2 > 0: 
            result += math.fabs(term1 * math.log(term1/term2))
    return result
    

def getDocNovality(doc):
    if doc not in reference_dict:
        return 0
    else:
        references = reference_dict[doc]
        references_size = len(references)
        if references_size == 0:
            return 0
        novality = 0
        for ref in references:
            novality += getKLDivergence(doc, ref)
        return novality/references_size
        


def calculateNovelityFeature():
    count = 0
    fin = open("./data_files/feature_paper_novality.txt", "w")
    for paper in year_dict:
        if count % 5000 == 0:
            print(count)
        novality = getDocNovality(paper)
        #print(novality)
        #return
        fin.write(str(paper) + "\t" + str(novality)+ "\n")
        count += 1
    fin.close()


calculateNovelityFeature()
print("Novality Feature Done !!!")