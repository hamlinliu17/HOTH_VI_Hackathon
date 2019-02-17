import pandas as pd
import numpy as np

footballData_17_18 = pd.read_csv("17_18.csv")
data_columns = footballData_17_18.columns

i = 0
while(i < len(data_columns)):
    if i >= 23:
        footballData_17_18.drop([data_columns[i]], axis = 1, inplace = True)
    i +=1

footballData_17_18.info()
