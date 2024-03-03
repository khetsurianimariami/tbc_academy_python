first_number = int(input("Please enter int number1: "))
second_number = int(input("Please enter int number2: "))

if first_number % second_number == 0:
    print(f"{first_number} is a multiple of {second_number}")
else:
    print(f"{first_number} isn't a multiple of {second_number}")
