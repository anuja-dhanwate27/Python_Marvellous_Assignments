import numpy as np
import pandas as pd

def main():
    data ={'Age':[18,22,25,30,35]}
    df = pd.DataFrame(data)
    original_val=df['Age']
    min_val=df['Age'].min()
    max_val=df['Age'].max()

    normalized = (original_val-min_val)/(max_val-min_val)
    print(normalized)

if __name__=="__main__":
    main() 