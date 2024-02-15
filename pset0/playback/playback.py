str = input()
for c in str:
    if c == ' ':
        print("...", end = '')
    else:
        print(c, end = '')
print()