from functools import reduce

def main():
    print("Enter the number of elements you want in a list:")
    size = int(input())
    Data = list()

    print("Enter ", size, " elements:")
    for i in range(size):
        value = int(input())
        Data.append(value)

    FData = list(filter(lambda Num: (Num >= 70 and Num <= 90), Data))
    print("Filtered Data : ", FData)

    MData = list(map(lambda Num : (Num + 10), FData))
    print("Mapped Data: ", MData)

    RData = reduce(lambda A, B: (A * B), MData)
    print("Reduced Data : ", RData)
    

    


if __name__ == "__main__":
    main()