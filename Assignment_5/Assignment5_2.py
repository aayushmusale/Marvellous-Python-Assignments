def ChkVowel(value):
    if(value == 'a' or value == 'e' or value == 'i' or value == 'o' or value == 'u'):
        return True
    else:
        return False

def main():
    print("Enter a character:")
    char = input()

    ret = ChkVowel(char)
    if(ret == True):
        print(char, " is a vowel")
    else:
        print(char, " is a consonant")

if __name__ == "__main__":
    main()