# factorial
def factorial(no):
    i = 1
    result = 1
    while i <= no:
        result *= i
        i += 1
    
    return result


def main():
    print("Enter a number: ")
    no = int(input())

    ans = factorial(no)
    print("Factorial of ", no, " is ", ans)


if __name__ == "__main__":
    main()