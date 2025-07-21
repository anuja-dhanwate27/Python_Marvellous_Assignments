import pandas as pd
def main():
   
   data = {'Name':['Amit','Sagar','pooja'],
            'Math':[85,90,78],
            'science':[92,88,80],
            'English':[75,85,82]
            }
   df = pd.DataFrame(data)
   df['Gender'] = ['Male','Male','Female']
   print(df)
   encode=pd.get_dummies(df[['Gender']])
   print(encode)
   

   


if __name__=="__main__":
   main()