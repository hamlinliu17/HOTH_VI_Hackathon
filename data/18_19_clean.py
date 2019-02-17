import pandas as pd
import numpy as np

footballData_18_19 = pd.read_csv("18_19.csv")

data_columns = footballData_18_19.columns

index = 0
while index < len(data_columns):
    if index >= 23:
        footballData_18_19.drop([data_columns[index]], axis = 1, inplace = True)
    index += 1


print(footballData_18_19.head())
