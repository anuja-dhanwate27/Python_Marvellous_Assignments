import pandas as pd
import matplotlib.pyplot as plt 

def main():
    data = {'Name':['Amit','Sagar','pooja'],
            'Math':[85,90,78],
            'science':[92,88,80],
            'English':[75,85,82]
            }
    df =pd.DataFrame(data)
    df['Total'] = df['Math'] + df['science'] +df['English']
    
    
    plt.bar(df['Name'],df['Total'])
    plt.xlabel(df['Name'])
    plt.ylabel(df['Total'])
    plt.title('Student bar plot')
    plt.show()





if __name__ =="__main__":
    main()
