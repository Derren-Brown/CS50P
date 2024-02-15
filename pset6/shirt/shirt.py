import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    if not (
        sys.argv[1].lower().endswith(".jpg" or ".jpeg" or ".png")
        and sys.argv[2].lower().endswith(".jpg" or ".jpeg" or ".png")
    ):
        print("Wrong format")
        sys.exit(1)
    root1, extension1 = os.path.splitext(sys.argv[1])
    root2, extension2 = os.path.splitext(sys.argv[2])
    if extension1 != extension2:
        print("Input and output have different extensions")
        sys.exit(1)
    try:
        img1 = Image.open(sys.argv[1])
    except FileNotFoundError:
        print("Input doesn't exist")
        sys.exit(1)
    else:
        shirt = Image.open("shirt.png")
        size = shirt.size
        img1 = ImageOps.fit(img1, size)
        img1.paste(shirt, shirt)
        img1.save(sys.argv[2])


if __name__ == "__main__":
    main()
