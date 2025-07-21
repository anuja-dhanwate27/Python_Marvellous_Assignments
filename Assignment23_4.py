import pandas as pd

def main():
    data = {'Name':['Amit','Sagar','pooja'],
            'Math':[85,90,78],
            'science':[92,88,80],
            'English':[75,85,82]
            }
    df =pd.DataFrame(data)
   
    Hdata = df[df['science']>85]
    print("The student who scored more than 85 is :")
    print(Hdata)




if __name__ =="__main__":
    main()
