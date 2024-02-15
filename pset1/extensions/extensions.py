def main():
    s = input("Expression: ")
    x, y, z = s.split(" ")
    x = int(x)
    z = int(z)
    match y:
        case '+':
            res = x + z
        case '-':
            res = x - z
        case '*':
            res = x * z
        case '/':
            res = x / z
    print(f"{res:.1f}")

if __name__ == "__main__":
    main()