import pandas as pd
import numpy as np

footballData= pd.read_csv("FootballData.csv")

data_columns = footballData.columns

index = 0
while index < len(data_columns):
    if index >= 23 or index <= 1:
        footballData.drop([data_columns[index]], axis = 1, inplace = True)
    index += 1

mapping = {
'Arsenal' : 0,
'Bournemouth' : 1,
'Brighton' : 2,
'Burnley' : 3,
'Cardiff' : 4,
'Chelsea' : 5,
'Crystal Palace' : 6,
'Everton' : 7,
'Fulham' : 8,
'Huddersfield' : 9,
'Leicester' : 10,
'Liverpool' : 11,
'Man City' : 12,
'Man United' : 13,
'Newcastle' : 14,
'Southampton' : 15,
'Tottenham' : 16,
'Watford' : 17,
'West Ham' : 18,
'Wolves' : 19,
'Stoke' : 20,
'Swansea' : 21,
'Watford' : 22,
'West Brom' : 23,
'Hull' : 24,
'Middlesbrough' : 25,
'Sunderland' : 26
}
footballData['HomeTeam'] = footballData['HomeTeam'].map(mapping)
footballData['AwayTeam'] = footballData['AwayTeam'].map(mapping)

footballData.drop(['Referee'], axis = 1, inplace = True)

mapping2 = {'H':1, 'A':-1, 'D':0}
footballData['HTR'] = footballData['HTR'].map(mapping2)
footballData['FTR'] = footballData['FTR'].map(mapping2)


data_columns2 = footballData.columns

list1 = []
for i in data_columns2:
    if((i != 'HomeTeam') and (i != 'AwayTeam')):
        list1 += [i]


Input_Matrix = footballData[['HomeTeam', 'AwayTeam']].as_matrix()
Result_Matrix= footballData[list1].as_matrix()
