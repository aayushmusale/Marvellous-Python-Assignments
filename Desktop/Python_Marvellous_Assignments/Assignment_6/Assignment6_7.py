
def Largest(numList):
    Max = 0
    for i in numList:
        if(Max < i):
            Max = i
    
    return Max 


def main():
    print("Enter total 5 numbers:")

    valueList = []
    for i in range(5):
        value = int(input())
        valueList.append(value)
    
    ret = Largest(valueList)
    print("Maximum number is : ", ret)


if __name__ == "__main__":
    main()