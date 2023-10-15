# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 13:56:03 2023

@author: osaic
"""

import pandas as pd

#read the file 
cube_df = pd.read_excel(r'C:\Users\osaic\Downloads\RT.xlsx',sheet_name='Sheet1')

#take the column start_time and change it to string using astype(str)function then take only 10 characters because they represent the date
cube_df['date_stripped'] = cube_df['START_TIME'].astype(str).str[:10]

#group by date_stripped and then with name of the cubes and use the sum function on the successful_rows column , our requirements is completed
new_df = cube_df.groupby(['date_stripped','Name']).agg({'SUCCESSFUL_ROWS':['sum']})

new_df.to_csv(r'C:\Users\osaic\Downloads\final_format.xlsx')

