

def main():
    print("Enter total elements in the list:")
    size = int(input())

    NumList = []
    print("Enter ", size, " elements: ")
    for i in range(size):
        value = int(input())
        NumList.append(value)
    
    EvenNumbers = list(filter(lambda num: (num % 2 == 0), NumList))
    print(EvenNumbers)


if __name__ == "__main__":
    main()