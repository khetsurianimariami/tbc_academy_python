text = input("Please enter string: ")

for i in range(0, len(text), 2):
    if text[i] != "e":
        print(text[i])
