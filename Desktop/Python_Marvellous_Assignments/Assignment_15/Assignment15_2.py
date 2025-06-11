import os


def main():
    print("Enter the name of the File: ")
    filename = input()

    fobj = open(filename, 'r')
    data = fobj.read()

    print(data)

    fobj.close()


if __name__ == "__main__":
    main()