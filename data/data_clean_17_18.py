import pandas as pd
import numpy as np

footballData_17_18 = pd.read_csv("17_18.csv")
data_columns = footballData_17_18.columns

i = 0
while(i < len(data_columns)):
    if i >= 23:
        footballData_17_18.drop([data_columns[i]], axis = 1, inplace = True)
    i +=1
footballData_17_18.drop(['Div'], axis = 1, inplace = True)
footballData_17_18.drop(['Date'], axis = 1, inplace = True)
footballData_17_18.drop(['Referee'], axis = 1, inplace = True)

data_columns2 = footballData_17_18.columns
mapping1 = {
    'Arsenal' : 0,
    'Bournemouth' : 1,
    'Burnley' : 3,
    'Brighton' : 2,
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
    'West Ham' : 18,
    'Stoke' : 20,
    'Swansea' : 21,
    'Watford' : 22
}
footballData_17_18['HomeTeam'] = footballData_17_18['HomeTeam'].map(mapping1)
footballData_17_18['AwayTeam'] = footballData_17_18['AwayTeam'].map(mapping1)

mapping2 = {
    'H' : 1,
    'A' : -1,
    'D' : 0
}
footballData_17_18['FTR'] = footballData_17_18['FTR'].map(mapping2)
footballData_17_18['HTR'] = footballData_17_18['FTR'].map(mapping2)

xMatrixList = []
for i in data_columns2:
    if i != 'FTR':
        xMatrixList += [i]

X = footballData_17_18[xMatrixList].as_matrix()
Y = footballData_17_18[['FTR']].as_matrix()
