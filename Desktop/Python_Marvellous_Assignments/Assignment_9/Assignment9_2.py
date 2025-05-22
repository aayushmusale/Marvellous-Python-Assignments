# Process to square a list of numbers using multiple processes
import multiprocessing
import os

def Square(DataList):
    # print("PID of Square task : ", os.getpid())
    # print("PID of Square process : ", os.getppid())
    for i in DataList:
        print(i**2)



def main():
    inputList = [10,11,12,13,14,15]

    Process1 = multiprocessing.Process(target=Square, args=(inputList,))
    # print("PID of main process : ", os.getpid())
    Process1.start()
    Process1.join()


if __name__ == "__main__":
    main()