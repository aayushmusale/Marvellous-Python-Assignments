import os

def ChkFile(Fname):
    ret = os.path.exists(Fname) 
    return ret

def main():
    print("Enter the name of the File: ")
    filename = input()

    ret = ChkFile(filename)
    if(ret):
        print(filename, "exits in the current directory")
    else:
        print(filename, "does not exists in the current directory")



if __name__ == "__main__":
    main()