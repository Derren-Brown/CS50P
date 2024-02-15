def main():
    while True:
        try:
            s = input("Fraction: ")
            x, y = s.split("/")
            fuel = int(x) / int(y)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if int(x) > int(y):
                pass
            else:
                break
    fuel = round(fuel * 100)
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")

if __name__ == "__main__":
    main()