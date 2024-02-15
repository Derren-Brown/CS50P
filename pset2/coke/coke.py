def main():
    due = 50
    while due > 0:
        while True:
            print(f"Amount Due: {due}")
            coin = int(input("Insert Coin: "))
            if coin == 25 or coin == 10 or coin == 5:
                break
        due -= coin
    print(f"Change Owed: {-due}")


if __name__ == "__main__":
    main()