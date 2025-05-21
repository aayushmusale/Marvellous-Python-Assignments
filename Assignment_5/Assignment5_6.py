def CelsiusToFahrenheit(C):
    F = 0
    F =  (C * 9/5) + 32
    return F


def main():
    print("Enter the temperature in Celsius: ")
    value = float(input())

    ret = CelsiusToFahrenheit(value)
    print("Temperature in Fahrenheit: ", ret)



if __name__ == "__main__":
    main()