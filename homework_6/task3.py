import random

THOUGHT_NUMBER = random.randint(0, 100)

i = 0
while i < 3:
    entered_number = int(input("Please input number between 0 and 99: "))
    if entered_number == THOUGHT_NUMBER:
        print("You are winner!!")
        break
    elif entered_number < THOUGHT_NUMBER:
        print("low")
        i += 1
        continue
    elif entered_number > THOUGHT_NUMBER:
        print("high")
        i += 1
        continue

else:
    print("Computer is winner")
