# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 12:39:53 2016

@author: 15IT60R19
"""

import sys
#import numpy as np
import matplotlib.pyplot as plt
#from scipy.stats.stats import pearsonr
import math
from math import sqrt
import matplotlib
import os
os.chdir("/home/other/15IT60R19/CitationPrediction")

path = "./data_files/"
filename = "result_year_9_real"
fileformat = ".txt"

######################################## Latexify Start#############################################
SPINE_COLOR = 'gray'

def latexify(fig_width=None, fig_height=None, columns=1):
    assert(columns in [1,2])

    if fig_width is None:
        fig_width = 5.39 if columns==1 else 6.9 # width in inches

    if fig_height is None:
        golden_mean = (sqrt(5)-1.0)/2.0    # Aesthetic ratio
        fig_height = fig_width*golden_mean # height in inches

    
    MAX_HEIGHT_INCHES = 10.0
    if fig_height > MAX_HEIGHT_INCHES:
        print("WARNING: fig_height too large:" + fig_height + 
              "so will reduce to" + MAX_HEIGHT_INCHES + "inches.")
        fig_height = MAX_HEIGHT_INCHES
   
    print fig_width
    print fig_height
    params = {'backend': 'ps',
              'text.latex.preamble': ['\usepackage{gensymb}'],
              'axes.labelsize': 12, # fontsize for x and y labels (was 10)
              'axes.titlesize': 12,
              'text.fontsize': 8, # was 10
              'legend.fontsize': 5.12, # was 10
              'xtick.labelsize': 12,
              'ytick.labelsize': 12,
              'text.usetex': True,
              'figure.figsize': [fig_width,fig_height],
              'font.family': 'serif'
    }

    matplotlib.rcParams.update(params)


def format_axes(ax):

    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    for spine in ['left', 'bottom']:
        ax.spines[spine].set_color(SPINE_COLOR)
        ax.spines[spine].set_linewidth(0.5)

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_tick_params(direction='out', color=SPINE_COLOR)

    return ax



######################################## Latexify #############################################






input1 = open(path + filename + fileformat,'r') # real dataset
#input2 = open(sys.argv[2],'r') # pure preferential
#input3 = open(sys.argv[3],'r') 
#input4 = open(sys.argv[4],'r') 
#input5 = open(sys.argv[5],'r') 

"""
citation_count_real_dataset= []
citation_frequency_real_dataset= []
citation_count_preferential= []
citation_frequency_preferential= []
citation_count_preferential_2= []
citation_frequency_preferential_2= []
citation_count_preferential_3= []
citation_frequency_preferential_3= []
citation_count_preferential_4= []
citation_frequency_preferential_4= []
"""
actual = []
predicted = []

for line in input1:
	line = line.rstrip().split('\t')
	actual.append(float(line[0]))
	predicted.append(float(line[1]))
"""
for line in input2:
	line = line.rstrip().split(':')
	citation_count_preferential.append(int(line[0]))
	citation_frequency_preferential.append(int(line[1]))


for line in input3:
        line = line.rstrip().split(':')
        citation_count_preferential_2.append(int(line[0]))
        citation_frequency_preferential_2.append(int(line[1]))


for line in input4:
        line = line.rstrip().split(':')
        citation_count_preferential_3.append(int(line[0]))
        citation_frequency_preferential_3.append(int(line[1]))

for line in input5:
        line = line.rstrip().split(':')
        citation_count_preferential_4.append(int(line[0]))
        citation_frequency_preferential_4.append(int(line[1]))
"""

latexify()
fig, ax = plt.subplots()

size = 2
#rects2 = ax.scatter(citation_count_preferential,citation_frequency_preferential,color='r',label='Standard preferential attachment',s=size)
#rects3 = ax.scatter(citation_count_preferential_collaboration,citation_frequency_preferential_collaboration,color='b',label='Collaborative preferential attachment',s=size)
#rects4 = ax.scatter(citation_count_delinking,citation_frequency_delinking,color='m',label='Iterated preferential \\ relay-cite',s=size)
#rects5 = ax.scatter(citation_count_delinking_collaboration,citation_frequency_delinking_collaboration,color='g',label='Iterated preferential collaborative relay-cite',s=size)
#Polya ($r_v =4000, d_v=1000, A=2$)
#IPRC ($\Theta = 0.8, A = 5$)

rects1 = ax.scatter(actual,predicted,color='red',label='Ground truth',s=size)
#rects2 = ax.scatter(citation_count_preferential,citation_frequency_preferential,color='g',label='PA',s=size)
#rects4 = ax.scatter(citation_count_preferential_3,citation_frequency_preferential_3,color='r',label='WSB',s=size)
#rects3 = ax.scatter(citation_count_preferential_2,citation_frequency_preferential_2,color='k',label='WYY',s=size)
#rects5 = ax.scatter(citation_count_preferential_4,citation_frequency_preferential_4,color='m',label='IPRC ($\Theta = 0.8, A=5$)',s=size)
#rects4 = ax.scatter(citation_count_preferential_3,citation_frequency_preferential_3,color='k',label='IPRCM ($r_v =4000, d_v=1000, A=2$)',s=size)

ax.set_xlabel('Actual Citation Count')
ax.set_ylabel('Predicted Citation Count')
#ax.set_yscale ('log')
#ax.set_xscale ('log')
#plt.ylim((-10.0,10000000))
#plt.xlim((0,100000))
#legend = plt.legend(handlelength = 0.6,handletextpad = .1, columnspacing =.30)
#plt.tight_layout()
format_axes(ax)
path = './plot/'+ filename +".pdf"
plt.savefig(path,bbox_inches='tight')
plt.show()