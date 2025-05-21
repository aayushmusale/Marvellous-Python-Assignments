def Display(num):
    for i in range(1, num+1):
        for j in range(i):
            print("*", end=" ")
        print()


def main():
    print("Enter a number")
    value = int(input())

    Display(value)

if __name__ == "__main__":
    main()