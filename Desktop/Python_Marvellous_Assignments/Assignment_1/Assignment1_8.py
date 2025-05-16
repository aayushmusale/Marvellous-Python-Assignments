def Display(no):
    for i in range(no):
        print("*\t", end="")


def main():
    print("Enter a number: ")
    num = int(input())
    Display(num)

if __name__ == "__main__":
    main()