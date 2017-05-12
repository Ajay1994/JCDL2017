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
import pickle
from scipy.signal import find_peaks_cwt



#Get the list of interested papers
fout = open("./data_files/interested_papers.txt","r")
year_dict = dict()
for line in fout:
    line_list = line.split("\t")
    year_dict[int(line_list[0])] = int(line_list[1])
fout.close()


#cretae the reference dictionary
fin = open("./data_files/citation_network.txt")
citation_dict = dict()
count = 0
for line in fin:
    try:
        list_line = line.strip("\n").split("\t")
        citer = int(list_line[0])
        cited = int(list_line[1])
        if cited not in year_dict or citer not in year_dict:
            continue
        year = int(year_dict[citer])
        if cited not in citation_dict:
            citation_dict[cited] = dict()
            for i in list(range(1970, 2011)):
                citation_dict[cited][i] = 0
            citation_dict[cited][year] += 1
        else:
            citation_dict[cited][year] += 1
    except:
        count += 1
fin.close()


citation_profile = dict()
for paper in citation_dict:
    citation_profile[paper] = []
    for i in list(range(year_dict[paper], 2011)):
        citation_profile[paper].append(citation_dict[paper][i])
        
        
others = []
normalized_citation_profile = dict()
for paper in citation_profile:
    max_val = max(citation_profile[paper])
    sum_val = sum(citation_profile[paper][:10])
    if sum_val == 0 or (float(sum_val) / len(citation_profile[paper])) <= 1:
        others.append(paper)
        continue
    normalized_citation_profile[paper] = []
    for val in citation_profile[paper]:
        normalized_citation_profile[paper].append(float(val) / max_val)
    

#normalized citation profile have papers > 1 average citation

def _getPeakCitationIndex(citation_profile):
    peaks = []
    if len(citation_profile) == 1:
        peaks.append(0)
        return peaks
    for index in list(range(0, len(citation_profile) - 1)):
        if citation_profile[index + 1] < citation_profile[index] and citation_profile[index] >= 0.75:
            peaks.append(index)
            
    if citation_profile[len(citation_profile) - 1] >= citation_profile[len(citation_profile) - 2] and citation_profile[len(citation_profile) - 1] >= 0.75:
        peaks.append(len(citation_profile) - 1)
    return peaks

_getPeakCitationIndex([0.05, 0.1, 0.15, 0.4, 0.25, 0.45, 0.45, 1.0, 0.55, 0.65, 0.65, 0.65, 0.25])


peakInit = []
peakMult = []
peakLate = []
monInc = []
monDec = []

for paper in normalized_citation_profile:
    peaks = _getPeakCitationIndex(normalized_citation_profile[paper])
    if len(peaks) > 1: #Multiple Peaks
        peakMult.append(paper)
    else:
        peak = peaks[0]
        if peak < 5: #Peak within first 5 years
            if peak == 0: #Peak within first year
                monDec.append(paper)
            else:
                peakInit.append(paper)
        else:
            last_year = len(normalized_citation_profile[paper]) - 1
            if peak == last_year:
                monInc.append(paper)
            else:
                peakLate.append(paper)
            

print('PeakInit : ', len(peakInit))
print('PeakMult : ', len(peakMult))
print('PeakLate : ', len(peakLate))
print('MonInc : ', len(monInc))
print('MonDec : ', len(monDec))


for i in list(range(0, 5)):
    plt.plot(citation_profile[monDec[i]])
plt.show()


out = open("./data_files/categories_new.txt", "w")
out1 = open("./data_files/category_peakinit_new.txt", "w")
out2 = open("./data_files/category_peaklate_new.txt", "w")
out3 = open("./data_files/category_peakmult_new.txt", "w")
out4 = open("./data_files/category_monInc_new.txt", "w")
out5 = open("./data_files/category_monDec_new.txt", "w")
for paper in peakInit:
    out.write(str(paper) + ",1\n")
    out1.write(str(paper) + ":"+ " ".join(str(x) for x in citation_profile[paper]) + "\n")
for paper in peakLate:
    out.write(str(paper) + ",2\n")
    out2.write(str(paper) + ":"+ " ".join(str(x) for x in citation_profile[paper]) + "\n")
for paper in peakMult:
    out.write(str(paper) + ",3\n")
    out3.write(str(paper) + ":"+ " ".join(str(x) for x in citation_profile[paper]) + "\n")
for paper in monInc:
    out.write(str(paper) + ",4\n")
    out4.write(str(paper) + ":"+ " ".join(str(x) for x in citation_profile[paper]) + "\n")
for paper in monDec:
    out.write(str(paper) + ",5\n")
    out5.write(str(paper) + ":"+ " ".join(str(x) for x in citation_profile[paper]) + "\n")
for paper in others:
    out.write(str(paper) + ",6\n")
out.close()
out1.close()
out2.close()
out3.close()
out4.close()
out5.close()

"""
fin = open("./data_files/feature_pc.txt")
paper_pc = dict()
for line in fin:
    paper_id = int(line.split("\t")[0])
    pc = float(line.split("\t")[1])
    paper_pc[paper_id] = pc
fin.close()

_file_type = "./data_files/category_peakinit.txt"
 
fin = open(_file_type, "r")


out = open("./data_files/category_monDec.txt")
infile = open("./data_files/_category_monDec.txt", "w")
for line in out:
    paperid = line.split(":")[0]
    citation_profile = line.split(":")[1]
    citation_profile = citation_profile.split(" ")
    if len(citation_profile) < 10:
        continue
    infile.write(paperid + ":" + " ".join(str(x) for x in citation_profile))
out.close()
infile.close()
"""
fin = open("./data_files/countX_data.txt")
paper_cx = dict()
line = 0
count = 0
value_arr = []
for line in fin:
    try:    
        paper_id = int(line.split(",")[0])
        pc = float(line.split(",")[1])
        if pc >= 3:
            count += 1
        value_arr.append(pc)
    except:
        continue
fin.close()
        


#Creation of the countX Dictioary
fout = open("./data_files/countX_raw_data.txt")
lineno = 0
fin = open("./data_files/countX_data.txt", "w")
for line in fout:
    try:
        if lineno % 5 == 0:
            paper_id = int(line.split(":")[1].strip())
        if lineno % 5 == 3:
            countXList = line.split(":")[1].strip()
            countXList = countXList.split(",")
        if lineno % 5 == 4:
            value = 0
            for v in countXList:
                try:
                    value += float(v)
                except:
                    continue
            fin.write(str(paper_id) + "," + str(value / (len(countXList) - 1)) + "\n")
        lineno += 1
    except:
        break
fout.close()

plt.hist(value_arr, bins=np.arange(min(value_arr), max(value_arr) + 0.2, 0.2))


