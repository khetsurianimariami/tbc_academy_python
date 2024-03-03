input_number = int(input("Please enter int number less or equal 10: "))

divisor = []

if input_number <= 10:
    if input_number % 2 == 0:
        divisor.append(2)
    if input_number % 3 == 0:
        divisor.append(3)
    if input_number % 5 == 0:
        divisor.append(5)
    if input_number % 7 == 0:
        divisor.append(7)
    print(divisor)
else:
    print("Please enter int number less or equal 10")


