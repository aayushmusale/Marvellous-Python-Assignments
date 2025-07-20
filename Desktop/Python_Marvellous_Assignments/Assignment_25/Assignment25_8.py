import pandas as pd
import numpy as np

def main():
    data = {'Marks' : [85, np.nan, 90, np.nan, 95]}
    df = pd.DataFrame(data)
    print(df)

    df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
    print(df)

if __name__ == "__main__":
    main()