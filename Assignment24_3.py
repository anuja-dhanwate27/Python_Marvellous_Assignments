import pandas as pd
def main():
   line="*"*50
   data = {'Name':['Amit','Sagar','pooja'],
            'Math':[85,90,78],
            'science':[92,88,80],
            'English':[75,85,82]
            }
   df = pd.DataFrame(data)
   df['Gender']=['Male','Male','Female']
   print(df)

   Marks=['Math','science','English']
   group_students=df.groupby('Gender')[Marks].mean()
   print(group_students)
   
   
   
   

if __name__=="__main__":
   main()