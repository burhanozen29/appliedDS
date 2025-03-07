# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 10:54:51 2025

@author: bozen
"""

# Pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np

df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv")
df.head(10)

#Identify and calculate the percentage of the missing values in each attribute
df.isnull().sum()/len(df)*100
df.dtypes

df['LaunchSite'].value_counts()
df['Orbit'].value_counts()
landing_outcomes = df['Outcome'].value_counts()

# index ile sıra
for i,outcome in enumerate(landing_outcomes.keys()):
    print(i,outcome)

#False ve none olanlar
bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])

landing_class = [0 if outcome in bad_outcomes else 1 for outcome in df['Outcome']]
df['Class']=landing_class
df[['Class']].head(8)

df["Class"].mean()
df.to_csv("dataset_part_2.csv", index=False)
