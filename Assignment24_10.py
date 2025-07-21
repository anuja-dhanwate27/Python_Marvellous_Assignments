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
   plt.boxplot(df['English'])
   plt.title('BoxPlot of english marks')
   plt.show()

   
   

if __name__=="__main__":
   main()