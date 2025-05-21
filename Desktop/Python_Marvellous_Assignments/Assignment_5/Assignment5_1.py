
def Addition(num1, num2):
    Ans = 0
    Ans = num1+num2
    return Ans

def Difference(num1, num2):
    Ans = 0
    Ans = num1-num2
    return Ans

def Product(num1, num2):
    Ans = 0
    Ans = num1*num2
    return Ans

def Division(num1, num2):
    Ans = 0
    Ans = num1/num2
    return Ans



def main():
    print("Enter two numbers:")
    value1 = int(input())
    value2 = int(input())
    
    ret = Addition(value1, value2)
    print("Sum: ", ret)

    ret = Difference(value1, value2)
    print("Difference: ", ret)

    ret = Product(value1, value2)
    print("Product: ", ret)

    ret = Division(value1, value2)
    print("Division: ", ret)


if __name__ == "__main__":
    main()