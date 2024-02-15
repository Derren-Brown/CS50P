import random


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            pass
    level = random.randint(1, level)
    while True:
        while True:
            try:
                n = int(input("Guess: "))
                if n > 0:
                    break
            except ValueError:
                pass
        if n > level:
            print("Too large!")
        elif n < level:
            print("Too small!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()
