
Count = 0
def CountZeros(no):
    global Count
    Digit = -1
    while(no > 0):
        Digit = int(no % 10)
        print(Digit)
        if(Digit == 0):
            Count += 1
        no = int(no / 10)
    
    return Count
    
    

def main():
    print("Enter the number: ")
    value = int(input())
    
    Ret =  CountZeros(value)
    print("Total zeros in ", value, " is : ", Ret)



if __name__ == "__main__":
    main()




    
    