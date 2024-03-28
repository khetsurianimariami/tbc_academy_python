text = input("Please input your text: ")
print("Input: ", text)
text = text.lower().replace(" ", "")

edited_text = ""

reversed_text = ""

letters = "qwertyuiopasdfghjklzxcvbnm"

for c in text:
    if c in letters:
        changed_text = edited_text + c

reversed_text = edited_text[::-1]

if reversed_text == edited_text:
    print("Output: Is palindrome")
else:
    print("Output: Isn't palindrome")
