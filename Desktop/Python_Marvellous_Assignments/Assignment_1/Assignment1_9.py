def DisplayEven():
    i = 1
    j = 0
    while(j < 10):
        if(i % 2 == 0):
            print(i, "\t", end="")
            j = j + 1

        i = i + 1

def main():
    DisplayEven()
    
if __name__ == "__main__":
    main()