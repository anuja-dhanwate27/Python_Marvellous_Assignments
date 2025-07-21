import pandas as pd
import matplotlib.pyplot as plt 

def main():
    data = {'Name':['Amit','Sagar','pooja'],
            'Math':[85,90,78],
            'science':[92,88,80],
            'English':[75,85,82]
            }
    df =pd.DataFrame(data)
    
    marks = df[df['Name']=='Amit'][['Math','science','English']].values.flatten()
    subjects = ['Math','science','English']

    
    plt.plot(subjects,marks,marker='o')
    plt.xlabel("Subjects")
    plt.ylabel("marks")
    plt.title("Amit report")
    plt.grid(True)
    plt.show()





if __name__ =="__main__":
    main()
