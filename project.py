# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:24:52 2021

@author: owner
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

marriedData = pd.read_excel('結婚人數.xlsx')
aboardData = pd.read_excel('歷年中華民國國民出國按年齡分.xlsx')

#整理結婚人數資料
marriedData = marriedData.drop(['結婚人數按性別、五歲年齡組及結婚次數分'], axis = 1)
marriedData = marriedData.head(49)
marriedData = marriedData.drop([0, 1, 2, 3], axis = 0)
tempFrame = {"year":[], "total":[], "-20":[], "20~29":[], "30~39":[], "40~49":[], 
             "50~59":[], "60+":[]}
temp = pd.DataFrame(tempFrame)

marriedColumns = list(marriedData.columns)
temp['year'] = marriedData[marriedColumns[0]]
temp['total'] = marriedData[marriedColumns[1]]
for i in range(2, 8):
    temp[list(tempFrame.keys())[i]] = \
    marriedData[marriedColumns[i]] + marriedData[marriedColumns[i + 13]] + \
    marriedData[marriedColumns[i + 1]] + marriedData[marriedColumns[i + 1]]
temp['year'] = temp['year'].astype(np.int64)
marriedData = temp
marriedData = marriedData.set_index('year')

#整理出國人數資料
aboardData.columns = ['year', 'total', '-12', '13~19', '20~29', '30~39', '40~49', '50~59', '60+']
aboardData = aboardData.drop([0], axis = 0)
aboardData['13~19'] += aboardData['-12']
aboardData = aboardData.rename(columns = {'13~19': '-20'})
aboardData = aboardData.drop(['-12'], axis = 1)

for i in range(1, len(aboardData.index)+1):
    aboardData['year'].loc[i] = int(str(aboardData['year'].loc[i])[-4:])
aboardData = aboardData.set_index('year')

colors1 = ['black', 'red', 'orange', 'blue', 'green', 'pink']
colors2 = ['pink', 'black', 'red', 'orange', 'blue', 'green']

for i, color1, color2 in zip(list(tempFrame.keys())[2:], colors1, colors2):    
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(marriedData.index, marriedData[i], color = color2, linewidth=2, marker='o')
    ax2.plot(aboardData.index, aboardData[i], color = color1, linewidth=2, marker='o')
    ax1.tick_params(axis='y')
    ax2.tick_params(axis='y')
    plt.title(i)
    plt.show()

