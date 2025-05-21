def Largest(num1, num2, num3):
    if(num1 > num2):
        if(num1 > num3):
            print(num1, " is the largest")
        else:
            print(num3, " is the largest")
    else:
        print(num2, " is the largest")


def main():
    print("Enter three numbers: ")
    value1 = int(input())
    value2 = int(input())
    value3 = int(input())
    
    Largest(value1,value2,value3)

if __name__ == "__main__":
    main()