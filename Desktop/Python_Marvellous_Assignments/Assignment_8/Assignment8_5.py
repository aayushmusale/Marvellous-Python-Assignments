import threading

def Display():
    print("1 to 50 : ")
    for i in range(1, 51):
        print(i, end=" ")
    print()


def DisplayReverse():
    print("50 to 1 : ")
    for i in range(50, 0, -1):
        print(i, end=" ")
    print()


def main():
    Thread1 = threading.Thread(target=Display)
    Thread2 = threading.Thread(target=DisplayReverse)

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()




if __name__ == "__main__":
    main()