
# def Power(no):
#     return no**2

Power = lambda a : a**2

def main():
    print("Enter a number : ")
    value = int(input())

    Ret = Power(value)
    print("Result : ", Ret)

if __name__ == "__main__":
    main()