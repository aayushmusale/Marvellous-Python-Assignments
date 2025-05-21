def CalculateArea(length, width):
    Ans = 0
    Ans = length * width
    return Ans


def CalculatePerimeter(length, width):
    Ans = 0
    Ans = (length+width)*2
    return Ans


def main():
    print("Enter length and breadth:")
    value1 = float(input())
    value2 = float(input())

    ret = CalculateArea(value1, value2)
    print("Area : ", ret)

    ret = CalculatePerimeter(value1, value2)
    print("Perimeter : ", ret)

if __name__ == "__main__":
    main()