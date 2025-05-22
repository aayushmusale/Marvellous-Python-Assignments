# factorial of numbers in a list
import multiprocessing

def factorial(No):
    Fact = 1
    for i in range(1, No+1):
        Fact = Fact * i
    
    return Fact


def main():
    Data = [10,11,12,13,14,15]
    p = multiprocessing.Pool()
    result = p.map(factorial, Data)

    p.close()
    p.join()

    print(result)

if __name__ == "__main__":
    main()
