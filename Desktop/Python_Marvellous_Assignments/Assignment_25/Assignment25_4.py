import pandas as pd
def main():
    data = {'Department' : ['HR', 'IT', 'Finance', 'HR', 'IT']}
    
    df = pd.DataFrame(data)
    print(df) 

    df = pd.get_dummies(df, columns=['Department'])
    print(df)

if __name__ == "__main__":
    main()