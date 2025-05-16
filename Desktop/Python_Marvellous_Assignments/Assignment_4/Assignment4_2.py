# lambda function which accepts two parameters and returns it's multiplication
Mult = lambda A,B : A * B

def main():
    print("Enter two numbers: ")
    num1 = int(input())
    num2 = int(input())

    Result = Mult(num1, num2)
    print("Multiplication : ", Result)

if __name__ == "__main__":
    main()