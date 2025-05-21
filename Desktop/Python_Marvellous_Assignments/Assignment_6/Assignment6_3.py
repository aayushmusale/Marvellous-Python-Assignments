def DisplayMultiplication(num):
    i = 1
    while(i <= 10):
        print(num, " x ", i, " = ", num * i)
        i += 1



def main():
    print("Enter a number:")
    value = int(input())

    DisplayMultiplication(value)

if __name__ == "__main__":
    main()