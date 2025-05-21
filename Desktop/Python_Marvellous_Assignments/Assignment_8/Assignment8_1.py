import threading

def DisplayEven():
    itr = 1
    i = 1
    print("First 10 Even Numbers : ", end="")
    while(i <= 10):
        if(itr % 2 ==  0):
            print(itr, end=" ")
            i = i + 1
        itr = itr + 1
    print()



def DisplayOdd():
    itr = 1
    i = 1
    print("First 10 Odd Numbers : ",  end="")
    while(i <= 10):
        if(itr % 2 !=  0):
            print(itr, end=" ")
            i = i + 1
        itr = itr + 1
    print()


def main():
    T1 = threading.Thread(target=DisplayEven)
    print("T1 is starting")
    T1.start()
    T1.join()           # join() method helps to execute the particular thread completely then the next thread will be run

    T2 = threading.Thread(target=DisplayOdd)
    print("T2 is starting")
    T2.start()
    T2.join()


if __name__ == "__main__":
    main()