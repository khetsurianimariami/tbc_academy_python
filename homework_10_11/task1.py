n = int(input("Please enter a natural number: "))

x = 0

for i in range(1, 2 * n, 4):
    x += 1 / i

for i in range(3, 2 * n, 4):
    x -= 1 / i

print("x = ", x * 4)
