height = int(input("Please enter christmas tree's height: "))

if height >= 3:
    print(" " * height, "*", " " * height)

    c = 1
    first_line = 3

    for i in range(height - 2):
        print(" " * int((height * 2 - first_line) / 2), "/" * c, "|", "\\" * c,
              " " * int((height * 2 - first_line) / 2))
        c += 1
        first_line += 2
    print(" " * height, "|", " " * height)

else:
    print("Please enter number between 3 and 50: ")
