import random

n = int(input("Please enter number between 0 and 30: "))
lst = []

if (n > 0) and (n < 30):
    for i in range(n):
        lst.append(random.randrange(0, 1000))
    print("lst = ", lst)
    print("max number = ", max(lst))

else:
    print("Please enter number between 0 and 30: ")




