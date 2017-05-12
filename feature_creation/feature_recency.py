# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 15:05:10 2016

@author: 15IT60R19
"""

import random
import sys
import os
os.chdir("/home/other/15IT60R19/CitationPrediction")
import numpy as np
from scipy.stats.stats import spearmanr, pearsonr
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

#Get the list of interested papers
fout = open("./data_files/interested_papers.txt","r")
year_dict = dict()
for line in fout:
    line_list = line.split("\t")
    year_dict[int(line_list[0])] = int(line_list[1])
fout.close()

fout = open("./data_files/feature_recency.txt", "w")
for paper in year_dict:
    fout.write(str(paper) + "\t" + str(2010 - year_dict[paper]))
    fout.write("\n")
fout.close()