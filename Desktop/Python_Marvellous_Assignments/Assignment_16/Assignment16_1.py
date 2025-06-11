


def main():
    fobj = open('student.txt', 'w')
    print("student.txt file created")

    print("Enter the names of 5 students: ")
    for i in range(5):
        name = input()
        fobj.write(name+"\n")
    
    fobj.close()


if __name__ == "__main__":
    main()