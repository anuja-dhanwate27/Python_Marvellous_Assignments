import pandas as pd

def main():
    data = {'Name':['Amit','Sagar','pooja'],
            'Math':[85,90,78],
            'science':[92,88,80],
            'English':[75,85,82]
            }
    df =pd.DataFrame(data)
   
    
    df['Total'] = df['Math'] + df['science'] +df['English']
    print("Data brfore sorting")
    print(df)

    sort = df.sort_values( by='Total', ascending=False)
    print("After sorted in descending order ")
    print(sort)



if __name__ =="__main__":
    main()
