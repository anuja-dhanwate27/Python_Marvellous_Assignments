import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def main():
    data={'Age':[25,30,45,35,22],'Salary':[50000,60000,80000,65000,45000],'purchased':[1,0,1,0,1]}
    df = pd.DataFrame(data)

    X = df[['Age','Salary']]
    Y = df['purchased']

    X_train,Y_train,X_test,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

    print("x_train data is:",X_train.shape)
    print("x_test data is:",X_test.shape)
    print("y_train data is:",Y_train.shape)
    print("y_test data is:",Y_test.shape)

if __name__=="__main__":
     main()