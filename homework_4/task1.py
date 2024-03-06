import random

players_number = int(input("Enter players number: "))

for i in range(players_number):
    print(random.randrange(1, 7), random.randrange(1, 7))

