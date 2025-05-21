import threading

def EvenFactors(num):
    Sum = 0
    itr = 1
    while(itr <= num):
        if(itr % 2 == 0):
            if(num % itr == 0):
                # print(itr, end=" ")
                Sum += itr
        itr += 1
    print("Sum of Even Factors of ", num, ":", Sum)

# 12 =  1 2 3 4 6
# odd 1 3 
# even 2 4 6 12
def OddFactors(num):
    Sum = 0
    itr = 1
    while(itr <= num):
        if(itr % 2 != 0):
            if(num % itr == 0):
                # print(itr, end=" ")
                Sum += itr
        itr += 1
    print("Sum of Odd Factors of ", num, ":", Sum)

    


def main():
    T1 = threading.Thread(target = EvenFactors, args=(12,))
    T1.start()
    T1.join()
    
    T2 = threading.Thread(target=OddFactors, args=(12,))
    T2.start()
    T2.join()

    print("exit from main")

if __name__ == "__main__":
    main()
