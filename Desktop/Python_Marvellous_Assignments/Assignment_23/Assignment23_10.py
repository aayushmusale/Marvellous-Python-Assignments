
import pandas as pd

def main():
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'], 'Math' : [85,90,75], 'Science' : [92,88,80], 'English' : [75,80,82]}

    df = pd.DataFrame(data)     # dataframe 'df' create

    df['Total'] = df['Math'] + df['Science'] + df['English']
    print(df)

    df.drop('English', axis=1, inplace=True)

    print("\nUpdated Dataframe : ")
    print(df)

            
if __name__ == "__main__":
    main()