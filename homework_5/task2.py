c = 1

for i in range(c, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}", end=" ")
    print()
    c += 1
