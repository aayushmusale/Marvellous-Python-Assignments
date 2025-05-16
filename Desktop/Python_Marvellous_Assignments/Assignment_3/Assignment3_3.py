def Min(numbers):
    # initialize value of the first indexed element to Min
    Min = int(numbers[0])
    for num in numbers:
        # Min = min(Min, int(num))
        if(Min > int(num)):
            Min = int(num)

    return Min

def main():
    print("Enter the number of elements you want: ")
    no = int(input())
    Numbers = list()

    print("Enter ", no, " elements:")
    for i in range(no):
        value = int(input())
        Numbers.append(value)
    
    MinResult = Min(Numbers)
    print("Minimum value is ", MinResult)



if __name__ == "__main__":
    main()