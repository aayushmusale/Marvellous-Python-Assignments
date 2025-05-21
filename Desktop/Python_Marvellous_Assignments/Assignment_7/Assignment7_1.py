
Square = lambda A : A*A
Cube = lambda A: A**3

def main():
    print("Enter a number : ")
    value = int(input())
    
    ret = Square(value)
    print("Square: ", ret)

    ret = Cube(value)
    print("Cube : ", ret)

if __name__ == "__main__":
    main()