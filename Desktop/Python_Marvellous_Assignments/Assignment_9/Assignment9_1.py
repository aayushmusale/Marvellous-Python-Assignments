import threading
import time

def Display1():
    for i in range(1,6):
        time.sleep(1)           #time delay for 1 second
        print(i, end=" ")
    print()

def Display2():
    for i in range(1,6):
        time.sleep(1)
        print(i, end=" ")
    print()

def Display3():
    for i in range(1,6):
        time.sleep(1)
        print(i, end=" ")
    print()

def main():
    Thread1 = threading.Thread(target=Display1)
    Thread2 = threading.Thread(target=Display2)
    Thread3 = threading.Thread(target=Display3)

    Thread1.start()    
    Thread1.join()

    # time.sleep(1)

    Thread2.start()
    Thread2.join()

    # time.sleep(1)

    Thread3.start()
    Thread3.join()

    # time.sleep(1)



if __name__ =="__main__":
    main()