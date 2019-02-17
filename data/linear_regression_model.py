from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import numpy as np
from data_clean_18_19 import *

Input_Matrix_train, Input_Matrix_test, Result_Matrix_train, Result_Matrix_test = train_test_split(Input_Matrix, Result_Matrix)

model = RandomForestClassifier(n_estimators = 100)

model.fit(Input_Matrix_train, Result_Matrix_train)

def predict(x1,x2):
    if(x1 == x2):
        return 0
    #Result_Matrix_Prediction = [[]]
    Result_Matrix_Prediction = model.predict([[x1,x2]])
    result = Result_Matrix_Prediction[0][2]
    return result

def winner():
    if(predict(x1,x2) == 1):
        return x1
    elif(predict(x1,x2) == 0):
        return 0
    else:
        return x2
