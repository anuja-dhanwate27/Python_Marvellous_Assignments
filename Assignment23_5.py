import pandas as pd

def main():
    data = {'Name':['Amit','Sagar','pooja'],
            'Math':[85,90,78],
            'science':[92,88,80],
            'English':[75,85,82]
            }
    df =pd.DataFrame(data)
    df['Name'] = df['Name'].replace('pooja','puja')
    print("After replacing the name")
    print(df)



if __name__ =="__main__":
    main()
