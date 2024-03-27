import math
import random

n = int(input("Please enter a natural number: "))

counter = 0
a = 0
b = 0

for i in range(0, n):
    a = random.random()
    b = random.random()

    if math.sqrt(a ** 2 + b ** 2) <= 1:
        counter += 1

print(4 * counter / n)
