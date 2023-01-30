#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:15:07 2022

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

sample_df['TS%'] = sample_df['PTS'] / (2 * (sample_df['FGA']+(0.44 * sample_df['FTA'])))

tspercentage_salary = sample_df[['TS%', 'SALARY (USD)']]

import seaborn as sns

sns.regplot(data=sample_df, x='TS%', y='SALARY (USD)', marker='+')

import numpy as np

x_values = sample_df['TS%']
y_values = sample_df['SALARY (USD)']

correlation_matrix = np.corrcoef(x_values, y_values)
r_value = correlation_matrix[0,1]

print(r_value)

