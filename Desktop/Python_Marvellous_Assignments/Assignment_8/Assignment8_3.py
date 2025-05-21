import threading

def EvenList(List1):
    Sum = 0
    for i in List1:
        if(i % 2 == 0):
            Sum = Sum + i
    print("Addition of Even Elements : ", Sum)


def OddList(List1):
    Sum = 0
    for i in List1:
        if(i % 2 != 0):
            Sum = Sum + i
    print("Addition of Odd Elements : ", Sum)


def main():
    InputList = [10,11,12,13,14,15]
    T1 = threading.Thread(target=EvenList, args=(InputList, ))      # 36
    T1.start()
    T1.join()

    T2 = threading.Thread(target=OddList, args=(InputList, ))       #39
    T2.start()
    T2.join()


if __name__ == "__main__":
    main()