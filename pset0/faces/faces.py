def main():
    s = input()
    s = convert(s)
    print(s)

def convert(s):
    if ':(' in s:
        s = s.replace(':(', '🙁')
    if ':)' in s:
        s = s.replace(':)', '🙂')
    return s

if __name__ == "__main__":
    main()