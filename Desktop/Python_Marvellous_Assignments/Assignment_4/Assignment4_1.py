Power = lambda A: A **2

def main():
    print("Enter the number:")
    num = int(input())

    Ret = Power(num)
    print("The Power of 2 of ", num, " is ", Ret)

if __name__ == "__main__":
    main()