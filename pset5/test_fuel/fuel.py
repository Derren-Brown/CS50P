def main():
    s = input("Fraction: ")
    percentage = convert(s)
    if percentage != -1:
        print(gauge(percentage))
    else:
        print("Error")

def convert(s):
    try:
        x, y = s.split("/")
        percentage = int(x) / int(y)
    except (ValueError, ZeroDivisionError):
        return -1
    else:
        if int(x) > int(y):
            return -1
        else:
            return round(100 * percentage)

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()