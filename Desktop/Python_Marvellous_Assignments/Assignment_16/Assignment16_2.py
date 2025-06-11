def main():
    fobj = open('student.txt', 'r')

    data = fobj.read()
    print(data)

    fobj.close()


if __name__ == "__main__":
    main()