
# def Double(num):
#     return num*2

def main():
    print("total no of elements in the list:")
    size = int(input())

    NumList = []
    print("Enter ", size, " elements: ")
    for i in range(size):
        value = int(input())
        NumList.append(value)
    
    # MData = list(map(Double, NumList))
    MData = list(map(lambda A: A*2, NumList))
    print(MData)



if __name__ == "__main__":
    main()