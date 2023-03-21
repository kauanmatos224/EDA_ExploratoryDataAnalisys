#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 12:02:39 2023

@author: kauan
"""


import pandas as pd

df = pd.read_csv('housing_full.csv')

print(df.head)



def unistats(df):
    #CREATE DATAFRAME WITH HEAD INFORMATION ABOUT NAME COLUNS
    output_df = pd.DataFrame(columns=['count', 'missing', 'unique', 'numeric',
                                      'dtype', 'mode', 'mean' , 'min', '25%', 
                                      'median', '75%', 'max', 'std', 'skew', 'kurt'])


    #PRINT VALUES STATS OF THE DATAFRAME VARIABLES AND MAKE DATAFRAME INVERSION
    for col in df:
        if pd.api.types.is_numeric_dtype(df[col]):
            output_df.loc[col] = [df[col].count(), 
                                  df[col].isnull().sum(),
                                  df[col].nunique(), 
                                  df[col].dtype, 
                                  pd.api.types.is_numeric_dtype(df[col]),
                                  df[col].mode().values[0], 
                                  df[col].mean(), 
                                  df[col].min(), 
                                  df[col].quantile(0.25), 
                                  df[col].median(), 
                                  df[col].quantile(0.75), 
                                  df[col].max(), 
                                  df[col].std(), 
                                  df[col].skew(),
                                  df[col].kurt()]
        else:
            output_df.loc[col] = [df[col].count(), 
                                  df[col].isnull().sum(), 
                                  df[col].nunique(), 
                                  df[col].dtype, 
                                  pd.api.types.is_numeric_dtype(df[col]), 
                                  df[col].mode().values[0], 
                                  '-', 
                                  '-',
                                  '-', 
                                  '-',
                                  '-', 
                                  '-', 
                                  '-', 
                                  '-', 
                                  '-']

    return output_df.sort_values(by=['numeric','skew', 'unique'], ascending=False)

df1 = unistats(df)





