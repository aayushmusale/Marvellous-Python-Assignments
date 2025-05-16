def Addition(numbers):
    Sum = 0
    for num in numbers:
        Sum += int(num)

    return Sum


def main():
    print("Enter the number of elements you want: ")
    no = int(input())
    Numbers = list()

    print("Enter ", no, " elements:")
    for i in range(no):
        value = input()
        Numbers.append(value)
    
    Ans = Addition(Numbers)
    print("Addition is ", Ans)

if __name__ == "__main__":
    main()