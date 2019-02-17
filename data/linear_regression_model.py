from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import numpy as np
from data_clean_18_19 import *

Input_Matrix_train, Input_Matrix_test, Result_Matrix_train, Result_Matrix_test = train_test_split(Input_Matrix, Result_Matrix)

model = RandomForestClassifier(n_estimators = 100)

model.fit(Input_Matrix_train, Result_Matrix_train)

def predict(x1,x2):
    Result_Matrix_Prediction = [[]]
    Result_Matrix_Prediction = model.predict([[x1,x2]])
    result = []
    i = 0
    while(i < 3):
        result += [Result_Matrix_Prediction[0][i]]
        i+=1
    return result


print(predict(0,13))
