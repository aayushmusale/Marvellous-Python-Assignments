import pandas as pd
import numpy as np


def main():
    data = {'City' : ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}

    df = pd.DataFrame(data)
    print(df)



if __name__ == "__main__":
    main()