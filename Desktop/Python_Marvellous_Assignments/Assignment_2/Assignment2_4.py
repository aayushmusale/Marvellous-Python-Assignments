# Addition of factors
def FactorSum(num):
    Sum = 0
    i = 1

    while(i <= num/2):
        if(num % i == 0):
            Sum += i 
        i += 1
    
    return Sum

def main():
    print("Enter a number:")
    no = int(input())

    ans = FactorSum(no)
    print("Factor Addition of ", no, " is ", ans)


if __name__ == "__main__":
    main()