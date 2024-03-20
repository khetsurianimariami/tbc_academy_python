text = input("Please enter your text: ")
text = text.lower()

action = input("Please enter action(e/d): ")

print("Entered text: ", text)
print("Entered action(e/d): ", action)

letters = "qwertyuiopasdfghjklzxcvbnm"

encrypted_text = ""

decrypted_text = ""

if action == "e":
    for c in text:
        if (c in letters) and (c != "p") and (c != "l") and (c != "m"):
            c = letters[letters.index(c) + 1]
            encrypted_text = encrypted_text + c

        elif (c == "p") or (c == "l") or (c == "m"):
            if c == "p":
                c = "q"
                encrypted_text = encrypted_text + c
            elif c == "l":
                c = "a"
                encrypted_text = encrypted_text + c
            else:
                c = "z"
                encrypted_text = encrypted_text + c

        else:
            encrypted_text = encrypted_text + c

    print("Encrypted text: ", encrypted_text)

if action == "d":
    for c in text:
        if (c in letters) and (c != "q") and (c != "a") and (c != "z"):
            c = letters[letters.index(c) - 1]
            decrypted_text = decrypted_text + c

        elif (c == "q") or (c == "a") or (c == "z"):
            if c == "q":
                c = "p"
                decrypted_text = decrypted_text + c
            elif c == "a":
                c = "l"
                decrypted_text = decrypted_text + c
            else:
                c = "m"
                decrypted_text = decrypted_text + c

        else:
            decrypted_text = decrypted_text + c

    print("Decrypted text: ", decrypted_text)
    