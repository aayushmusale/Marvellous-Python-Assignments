import time
import threading
import multiprocessing

def Addition():
    Sum = 0
    for i in range(0, 10000001):
        Sum += i
    return Sum

def Addition1():
    Sum = 0
    for i in range(0, 10000001):
        Sum += i
    print("Addition : ", Sum)


def main():
    # normal function
    start_time = time.time()

    ans = Addition()
    print("Addition : ", ans)

    end_time = time.time()

    print("Time required using normal function : ", end_time - start_time)

    # threading
    start_time = time.time()
    T1 = threading.Thread(target=Addition1)
    T1.start()
    T1.join()

    end_time = time.time()

    print("Time required using Threading : ", end_time - start_time)

    # multiprocessing
    start_time = time.time()
    P1 = multiprocessing.Process(target=Addition1)
    P1.start()
    P1.join()

    end_time = time.time()

    print("Time required using multiprocessing : ", end_time - start_time)
    



if __name__ == "__main__":
    main()