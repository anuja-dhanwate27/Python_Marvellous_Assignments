import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    data = {'Name':['Amit','Sagar','pooja'],
            'Math':[85,90,78],
            'science':[92,88,80],
            'English':[75,85,82]
            }
    df =pd.DataFrame(data)
    
    df.drop(columns = 'English' ,inplace = True)
    print(df)

if __name__=="__main__":
    main()




