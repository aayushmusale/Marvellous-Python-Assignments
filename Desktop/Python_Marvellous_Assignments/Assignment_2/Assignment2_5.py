# prime number
def CheckPrime(num):
    i = 2
    bFlag = True
    while i <= num/2:
        if(num % i == 0):
            bFlag = False
        
        i += 1
    
    return bFlag

def main():
    print("Enter a number: ")
    no = int(input())

    result = CheckPrime(no)
    if(result == True):
        print(no, " is a Prime Number")
    else:
        print(no, " is not a Prime Number")


if __name__ == "__main__":
    main()