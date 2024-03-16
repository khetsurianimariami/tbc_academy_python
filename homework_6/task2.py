PASSWORD = "python"

for i in range(3):
    input_password = input("Please enter password: ")
    if input_password == PASSWORD:
        print("You are right!")
        break
    else:
        continue
