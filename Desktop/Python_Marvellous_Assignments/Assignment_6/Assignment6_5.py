
def ChkPrime(num):
    i = 2
    while(i <= int(num/2)):
        if(num % i == 0):
            return False
        i += 1
    
    return True


def main():
    print("Enter a number: ")
    value = int(input())

    ret = ChkPrime(value)
    if(ret == True):
        print(value, " is a prime number")
    else:
        print(value, " is not a prime number")


if __name__ == "__main__":
    main()