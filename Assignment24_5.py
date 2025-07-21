import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def main():
   line="*"*50
   data = {'Name':['Amit','Sagar','pooja'],
            'Math':[85,90,78],
            'science':[92,88,80],
            'English':[75,85,82]
            }
   df = pd.DataFrame(data)
   
   df['Total'] = df['Math'] + df['science'] +df['English']

   print("Total marks are:")
   print(df)

   df['Status']=df['Total'].apply(lambda x: 'pass' if x>=250 else 'fail')
   print("Display the pass or fail status")
   print(df)

 
if __name__=="__main__":
   main()