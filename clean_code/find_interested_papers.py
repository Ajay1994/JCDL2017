# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:31:27 2016

@author: ajay
"""

import sys
import os
os.chdir("/home/ajay/CitationPrediction/")
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

fout = open("./data_files/paper_abstract","r")
abstract_papers = set()
for line in fout:
    paper_id = int(line.split("\t")[0])
    abstract_papers.add(paper_id)
fout.close()

fout = open("./data_files/paper_title","r")
title_papers = set()
for line in fout:
    paper_id = int(line.split("\t")[0])
    title_papers.add(paper_id)
fout.close()


fout = open("./data_files/paper_years_final","r")
year_papers = set()
year_dict = dict()
for line in fout:
    line_list = line.split("\t")
    year_papers.add(int(line_list[0]))
    year_dict[int(line_list[0])] = int(line_list[1])
fout.close()

fout = open("./data_files/authors_paper.txt","r")
author_papers = set()
for line in fout:
    paper_id = int(line.split("\t")[1])
    author_papers.add(paper_id)
fout.close()


# Find intersection of all dataset : create filterted dataset
# Considering papers from 1970 - 2010
fin = open("./data_files/interested_papers.txt", "w")
for paper in title_papers:
    if paper in abstract_papers and paper in year_papers and paper in author_papers:
        if year_dict[paper] >= 1970 and year_dict[paper] <= 2010:
            fin.write(str(paper) + "\t" + str(year_dict[paper]) + "\n")
fin.close()


#Count of papers within 2000 and above 2000
count_less_2000 = 0
count_above_2000 = 0
for paper in year_dict:
    if year_dict[paper] <= 2000:
        count_less_2000 += 1
    else:
        count_above_2000 += 1