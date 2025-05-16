def CalculateDigits(num):
    Digits = 0
    for i in num:
        Digits += 1

    return Digits


def main():
    print("Enter a number :")
    no = str(input())

    result = CalculateDigits(no)
    print("Number of the Digits in ", no, " is ", result)


if __name__ == "__main__":
    main()