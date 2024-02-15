def main():
    ans = input("Greeting: ")
    ans = ans.strip().lower()
    if ans.startswith('hello'):
        print('$0')
    elif ans.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()