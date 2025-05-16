import Arithmetic

def main():
    print("Enter first number")
    num1 = int(input())

    print("Enter second number")
    num2 = int(input())

    result = Arithmetic.Add(num1, num2)
    print("Addition: ", result)

    result = Arithmetic.Sub(num1, num2)
    print("Subtraction: ", result)

    result = Arithmetic.Div(num1, num2)
    print("Division: ", result)

    result = Arithmetic.Mult(num1, num2)
    print("Multipliaction: ", result)
    
 

if __name__ == "__main__":
    main()