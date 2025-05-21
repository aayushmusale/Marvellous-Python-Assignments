import threading

# display all small letters from the string 
def CalculateSmall(StringValue):
    Cnt = 0
    print("Thread ID of small thread is : ", threading.get_ident())
    print("Thread name of small thread is : ", threading.current_thread().name)
    for i in StringValue:
        temp = ord(i)           #converts the character into its ASCII code value
        if(temp >= 97 and temp <= 122):
            Cnt = Cnt + 1
    
    print("No. of Small letters : ", Cnt)


# display all captial letters from the string 
def CalculateCapital(StringValue):
    Cnt = 0
    print("Thread ID of capital thread is : ", threading.get_ident())
    print("Thread name of capital thread is : ", threading.current_thread().name)
    for i in StringValue:
        temp = ord(i)           #converts the character into its ASCII code value
        if(temp >= 65 and temp <= 90):
            Cnt = Cnt + 1
    
    print("No. of Capital letters : ", Cnt)




# display all digits from the string 
def CalculateDigits(StringValue):
    Cnt = 0
    print("Thread ID of digits thread is : ", threading.get_ident())
    print("Thread name of digits thread is : ", threading.current_thread().name)
    for i in StringValue:
        temp = ord(i)           #converts the character into its ASCII code value
        if(temp >= 48 and temp <= 57):
            Cnt = Cnt + 1
    
    print("No. of Digits : ", Cnt)


def main():
    print("Thread ID of main thread is : ", threading.get_ident())
    print("Thread name of main thread is : ", threading.current_thread().name)
    print()
    inputString = "A906 Gokhale Business Bay"
    # print(inputString)

    small = threading.Thread(target=CalculateSmall, args=(inputString, ))
    capital = threading.Thread(target=CalculateCapital, args=(inputString,))
    digits = threading.Thread(target=CalculateDigits, args=(inputString,))
    

    small.start()
    small.join()
    print()

    capital.start()
    capital.join()
    print()

    digits.start()
    digits.join()
    print()
    
    



if __name__ == "__main__":
    main()
