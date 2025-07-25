import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    data = {'Age' : [22, 25, 47, 52, 46, 56],
            'Purchased' : [0, 1, 1, 0, 1, 0]}
    
    df = pd.DataFrame(data)
    print(df) 

    x = df['Age']
    y = df['Purchased']

    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=42)

    print("Dimensions of Training dataset : ",x_train.shape)
    print("Dimensions of Testing dataset : ",x_test.shape)


if __name__ == "__main__":
    main()