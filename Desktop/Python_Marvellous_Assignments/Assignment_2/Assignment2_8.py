def Display(num):
    for i in range(num+1):
        for j in range(i):
            print(j+1, end="\t")
        print()
        



def main():
    print("Enter a number :")
    no = int(input())

    Display(no)


if __name__ == "__main__":
    main()