text = input("Please enter word: ")
consonants = "bcdfghjklmnpqrstvwxz"

for i in range(0, len(text)):
    if text[i].lower() in consonants:
        print(text[i], end=" ")
