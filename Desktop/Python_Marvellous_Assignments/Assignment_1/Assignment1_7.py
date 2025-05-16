def isDivisible(no):
    if(no % 5 == 0):
        return True
    return False



def main():
    print("Enter a number: ")
    num = int(input())
    
    result = isDivisible(num)
    if(result == True):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()