text = input("Please enter word: ")
text = text.replace(" ", "")

if len(text) % 2 == 1:
    i = 0
    while i < len(text):
        if (i == 0) or (i == (len(text) - 1)) or (i == (len(text) // 2)):
            print(text[i] * 5, end=" ")
        i += 1

else:
    i = 0
    while i < len(text):
        if (i == 0) or (i == (len(text) - 1)) or (i == (len(text) / 2)) or (i == (len(text) / 2 - 1)):
            print(text[i] * 5, end=" ")
        i += 1
