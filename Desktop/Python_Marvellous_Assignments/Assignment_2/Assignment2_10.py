def DigitAddition(num):
    Sum = 0
    for i in num:
        Sum += int(i)

    return Sum


def main():
    print("Enter a number :")
    no = str(input())

    result = DigitAddition(no)
    print("Addition of the Digits of ", no, " is ", result)


if __name__ == "__main__":
    main()