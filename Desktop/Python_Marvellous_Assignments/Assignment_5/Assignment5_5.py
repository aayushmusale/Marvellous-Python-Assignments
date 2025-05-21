def ChkEven(num):
    if(num % 2 == 0):
        return True
    else:
        return False

def main():
    print("Enter a number:")
    value = int(input())

    ret = ChkEven(value)
    if( ret == True):
        print(value, " is a even number")
    else:
        print(value, " is an odd number")

if __name__ == "__main__":
    main()