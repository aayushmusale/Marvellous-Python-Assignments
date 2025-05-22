
Fact = 1
def Factorial(no):
    global Fact
    if(no >= 1):
        Fact = Fact * no
        no = no - 1
        Factorial(no)
    return Fact

def main():
    print("Enter the number: ")
    value = int(input())
    
    Ret = Factorial(value)
    print("Factorial of ", value, " is : ", Ret)



if __name__ == "__main__":
    main()