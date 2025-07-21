import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    data = {'Name':['Amit','Sagar','pooja'],
            'Math':[85,90,78],
            'science':[92,88,80],
            'English':[75,85,82]
            }
    df =pd.DataFrame(data)
    
    data2 = {'Name':['Amit','Sagar','pooja'],
            'Math':[np.nan,90,78],
            'science':[92,np.nan,80],
            
            }
    df2 =pd.DataFrame(data2)
    df2[['Math','science']] = df2[['Math','science']].fillna(df[['Math','science']].mean())
    print(df2)


if __name__ =="__main__":
    main()

    
