def Display(no):
    for i in range(no):
        for j in range(no):
            print("*", end="\t")
        print()

        
def main():
    print("Enter a number: ")
    no = int(input())

    Display(no)

if __name__ == "__main__":
    main()