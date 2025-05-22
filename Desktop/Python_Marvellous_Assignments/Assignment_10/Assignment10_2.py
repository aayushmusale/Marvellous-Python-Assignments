Mult = lambda no1, no2 : no1 * no2

def main():
    print("Enter two numbers: ")
    value1 = int(input())
    value2 = int(input())

    Ret = Mult(value1, value2)
    print("Result : ", Ret)
    
if __name__ == "__main__":
    main()