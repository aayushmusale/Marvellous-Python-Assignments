def ChkNum(no):
    if(no < 0):
        print(no, ": Negative Number")
    elif(no == 0):
        print(no, ": Zero")
    else:
        print(no, ": Positive Number")

def main():
    print("Enter a number :")
    num = int(input())
    ChkNum(num)

if __name__ == "__main__":
    main()