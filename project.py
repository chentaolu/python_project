# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:24:52 2021

@author: owner
"""

import pandas as pd
import matplotlib.pyplot as plt

marriedData = pd.read_excel('結婚人數.xlsx')
aboardData = pd.read_excel('歷年中華民國國民出國按年齡分.xlsx')

#整理結婚人數資料
marriedData = marriedData.drop(['結婚人數按性別、五歲年齡組及結婚次數分'], axis = 1)
marriedData = marriedData.drop([0, 3, 143, 144], axis = 0)

#整理出國人數資料
aboardData.columns = ['year', 'total', '12-', '13~19', '20~29', '30~39', '40~49', '50~59', '60+']
aboardData = aboardData.drop([0], axis = 0)

for i in range(1, len(aboardData.index)+1):
    aboardData['year'].loc[i] = int(str(aboardData['year'].loc[i])[-4:])
aboardData = aboardData.set_index('year')

print(marriedData)