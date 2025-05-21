
def isEligible(age):
    if(age >= 18):
        return True
    else:
        return False


def main():
    print("Enter the age:")
    age = int(input())

    ret = isEligible(age)
    if(ret == True):
        print("Eligible to vote")
    else:
        print("Not eligible to vote, age should be 18 or above")
   

if __name__ == "__main__":
    main()