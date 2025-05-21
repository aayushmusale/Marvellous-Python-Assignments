from functools import reduce

def main():
    print("Enter total elements in the list:")
    size = int(input())

    NumList = []
    print("Enter ", size, " elements: ")
    for i in range(size):
        value = int(input())
        NumList.append(value)
    
    RData = reduce(lambda A,B: A*B, NumList)
    print("Product : ",RData)


if __name__ == "__main__":
    main()