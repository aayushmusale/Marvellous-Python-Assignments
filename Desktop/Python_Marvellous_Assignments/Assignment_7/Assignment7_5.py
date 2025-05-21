def  ChkPalindrome(value):
    size = len(value)
    i = 0
    j = size-1
    

    while(i <= j):
        if(value[i] != value[j]):
            return False
    
        i += 1
        j -= 1
    
    return True


def main():
    print("Enter the string: ")
    String = input()

    Result = ChkPalindrome(String)
    if(Result == True):
        print(String, " is a palindrome")
    else:
        print(String, " is not a palindrome")



if __name__ == "__main__":
    main()