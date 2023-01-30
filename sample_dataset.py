#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 16:53:03 2022

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

sample_df['TS%'] = (sample_df['PTS'] / (2 * (sample_df['FGA']+(0.44 * sample_df['FTA']))))*100

sample_df.drop(['GP','MIN','FG%','3PM','3PA','FT%','DD2','TD3'], axis = 1, inplace = True)

print(sample_df)

