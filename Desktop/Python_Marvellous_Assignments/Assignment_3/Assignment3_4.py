def Frequency(NumList, num):
    freq = 0
    for i in NumList:
        if(num == int(i)):
            freq += 1
    
    return freq



def main():
    print("Enter the number of elements you want:")
    size = int(input())
    Numbers = list()

    print("Enter ", size, " elements: ")
    for i in range(size):
        value = int(input())
        Numbers.append(value)

    print("Enter the number whose frequency you want: ")
    no = int(input())

    Result = Frequency(Numbers, no)
    print("The Frequency of ", no, " is ", Result)



if __name__ == "__main__":
    main()