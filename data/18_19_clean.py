import pandas as pd
import numpy as np

footballData_18_19 = pd.read_csv("18_19.csv")

data_columns = footballData_18_19.columns

index = 0
while index < len(data_columns):
    if index >= 23 or index <= 1:
        footballData_18_19.drop([data_columns[index]], axis = 1, inplace = True)
    index += 1


print(footballData_18_19.head())

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
'Wolves' : 19
}
footballData_18_19['HomeTeam'] = footballData_18_19['HomeTeam'].map(mapping)
footballData_18_19['AwayTeam'] = footballData_18_19['AwayTeam'].map(mapping)

footballData_18_19.drop(['Referee'], axis = 1, inplace = True)

mapping2 = {'H':1, 'A':-1, 'D':0}
footballData_18_19['HTR'] = footballData_18_19['HTR'].map(mapping2)
footballData_18_19['FTR'] = footballData_18_19['FTR'].map(mapping2)

data_columns2 = footballData_18_19.columns

list1 = []
for i in data_columns2:
    if i != 'FTR':
        list1 += [i]

print(list1)

x = footballData_18_19[list1].as_matrix()
y = footballData_18_19[['FTR']].as_matrix()

print(x)
print(y.shape)
