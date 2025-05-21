def DisplayEvenSum(num1, num2):
    Sum = 0
    while(num1 <= num2):
        if(num1 % 2 == 0):
            Sum += num1
            
        num1 += 1
    
    return Sum


def main():
    ret = DisplayEvenSum(1, 100)
    print("Sum of even numbers between 1 to 100 is :", ret)

if __name__ == "__main__":
    main()