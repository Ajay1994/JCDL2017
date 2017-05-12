# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 23:25:50 2016

@author: ajay
"""

import sys
import os
os.chdir("/home/other/15IT60R19/CitationPrediction")
import numpy as np
from scipy.stats.stats import spearmanr, pearsonr


# Creation of the countX feature

fout = open("/home/other/15IT60R19/data_files/countX_raw_data.txt")
fin = open("./data_files/countX_feature.txt", "w")
fin.write("paper_id,countX\n")
lineno = 0
for line in fout:
    try:
        if lineno % 5 == 0:
            paper_id = int(line.split(":")[1].strip())
        if lineno % 5 == 3:
            countXList = line.split(":")[1].strip()
            countXList = countXList.split(",")
        if lineno % 5 == 4:
            countX = 0
            if float(countXList[0]) == 0.0:
                countX = float(countXList[1])
            else:
                countX = (float(countXList[0]) + float(countXList[1]) + float(countXList[2]))
            fin.write(str(paper_id) + "," + str(countX) + "\n")
            fin.flush()
        lineno += 1
    except:
        continue
fin.close()
fout.close()

#Creation of Citewords Features

fout = open("./data_files/citewords_raw_data.txt")
fin = open("./data_files/citewords_feature.txt", "w")
fin.write("paper_id,citewords\n")
lineno = 0
for line in fout:
    try:
        if lineno % 5 == 0:
            paper_id = int(line.split(":")[1].strip())
        if lineno % 5 == 3:
            citewordList = line.split(":")[1].strip()
            citewordList = citewordList.split(",")
        if lineno % 5 == 4:
            citeword = 0
            if float(citewordList[0]) == 0.0:
                citeword = float(citewordList[1])
            else:
                citeword = (float(citewordList[0]) + float(citewordList[1]) + float(citewordList[2]))
            fin.write(str(paper_id) + "," + str(citeword) + "\n")
            fin.flush()
        lineno += 1
    except:
        continue
fin.close()
fout.close()
