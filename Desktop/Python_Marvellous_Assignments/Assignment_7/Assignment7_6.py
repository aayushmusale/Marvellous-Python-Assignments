def ChkPrime(num):
    i = 2
    while(i <= int(num/2)):
        if(num % i == 0):
            return False

        i += 1
        
    return True


def main():
    print("Enter total elements in the list:")
    size = int(input())

    NumList = []
    print("Enter ", size, " elements: ")
    for i in range(size):
        value = int(input())
        NumList.append(value)
    
    RData = list(filter(ChkPrime, NumList))
    print("Prime Numbers : ",RData)


if __name__ == "__main__":
    main()