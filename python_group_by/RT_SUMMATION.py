# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 06:33:37 2023

@author: krisja6
"""


import pandas as pd
import datetime as dt



strin = "C:\\Users\\krisja6\\Downloads\\"
df =pd.read_excel(strin+"RT.xlsx",sheet_name="Sheet1")

lis = df['START_TIME'].tolist()
lis2=[]
for i in lis:
    lis2.append(i.date())
    
df['Date'] = lis2

#print(df.head())

grouped_multiple = df.groupby(['Date', 'Name']).agg({'SUCCESSFUL_ROWS': ['sum', 'min']})
grouped_multiple.columns = ['age_Sum', 'age_min']
grouped_multiple = grouped_multiple.reset_index()
print(type(grouped_multiple))

#grouped_multiple.to_excel(r'C:\\Users\\krisja6\\Downloads\\RT_sessions.xlsx', index=False)
