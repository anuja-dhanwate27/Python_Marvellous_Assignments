import pandas as pd

def main():
    data = {'Name':['Amit','Sagar','pooja'],
            'Math':[85,90,78],
            'science':[92,88,80],
            'English':[75,85,82]
            }
    df = pd.DataFrame(data)

    print("Shapes:",df.shape)
    print("Columns:",df.columns)
    print("Data type:",df.dtypes)



if __name__ == "__main__":
    main()