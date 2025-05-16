def Max(numbers):
    Max = 0
    for num in numbers:
        # Max = max(Max, int(num))
        if(Max < int(num)):
            Max = int(num)

    return Max

def main():
    print("Enter the number of elements you want: ")
    no = int(input())
    Numbers = list()

    print("Enter ", no, " elements:")
    for i in range(no):
        value = int(input())
        Numbers.append(value)
    
    MaxResult = Max(Numbers)
    print("Maximum value is ", MaxResult)


if __name__ == "__main__":
    main()