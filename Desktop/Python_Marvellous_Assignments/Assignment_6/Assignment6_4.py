
def Factorial(num):
    Fact = 1
    for i in range(1, num+1):
        Fact = Fact * i
    
    return Fact


def main():
    print("Enter a number : ")
    value = int(input())

    ret = Factorial(value)
    print("Factorial of ", value, " is : ", ret)


if __name__ == "__main__":
    main()