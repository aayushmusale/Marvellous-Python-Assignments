import MarvellousNum

def ListPrime(NumList):
    SumPrime = 0
    for num in NumList:
        if(MarvellousNum.CheckPrime(int(num)) == True):
            SumPrime += int(num)

    return SumPrime

def main():
    print("Enter the number of elements you want:")
    size = int(input())
    Numbers = list()

    print("Enter ", size, " elements: ")
    for i in range(size):
        value = int(input())
        Numbers.append(value)


    Result = ListPrime(Numbers)    
    print("Addition of the Prime numbers from the list: ", Result)
    


if __name__ == "__main__":
    main()