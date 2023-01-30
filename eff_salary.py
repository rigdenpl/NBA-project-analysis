#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:25:55 2022

@author: rigdenlama
"""
import pandas as pd

df = pd.read_csv(r'/Users/rigdenlama/Desktop/Math IA/ESPN database.csv')

names = ['Trae Young', 
'Kyrie Irving',
'LaMelo Ball',
'Kemba Walker',
'Stephen Curry',
'Luka Doncic',
'Jamal Murray',
'Ja Morant',
'Dejounte Murray',
'Chris Paul',
'Damian Lillard',
'John Wall',
'Russell Westbrook',
'Ben Simmons',
"De'Aaron Fox",
'Kyle Lowry',
'Jrue Holiday',
'Darius Garland',
'Coby White',
"D'Angelo Russell",
'Mike Conley',
'Malcolm Brogdon',
'Tyler Herro',
'Dennis Schroder',
'Eric Bledsoe',
'Cole Anthony',
'Patrick Beverley',
'Shai Gilgeous-Alexander',
'Elfrid Payton',
'Delon Wright']

sample_df = df[df.NAME.isin(names)]

sample_df['Missed FG'] = sample_df['FGA'] - sample_df['FGM']

sample_df['Missed FT'] = sample_df['FTA'] - sample_df['FTM']

sample_df['EFF'] = sample_df['PTS'] + sample_df['REB'] + sample_df['AST'] + sample_df['STL'] + sample_df['BLK'] - sample_df['Missed FG'] - sample_df['Missed FT'] - sample_df['TO']

eff_salary = sample_df[['EFF', 'SALARY (USD)']]

import seaborn as sns

sns.regplot(data=sample_df, x='EFF', y='SALARY (USD)', marker='+')

import numpy as np

x_values = sample_df['EFF']
y_values = sample_df['SALARY (USD)']

correlation_matrix = np.corrcoef(x_values, y_values)
r_value = correlation_matrix[0,1]

print(r_value)