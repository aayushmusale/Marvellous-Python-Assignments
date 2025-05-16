# FMR using normal functions
from functools import reduce

def ChkPrime(num):
    bFlag = True
    i = 2
    while i <= (num/2):
        if(num % i == 0):
            bFlag = False
        i += 1
    
    return bFlag

def Mult(num):
    return num * 2

def Max(num1, num2):
    return max(num1, num2)

def main():
    print("Enter the number of elements you want in a list:")
    size = int(input())
    Data = list()

    print("Enter ", size, " elements:")
    for i in range(size):
        value = int(input())
        Data.append(value)

    FData = list(filter(ChkPrime, Data))
    print("Filtered Data : ", FData)

    MData = list(map(Mult, FData))
    print("Mapped Data: ", MData)

    RData = reduce(Max, MData)
    print("Reduced Data : ", RData)


if __name__ == "__main__":
    main()