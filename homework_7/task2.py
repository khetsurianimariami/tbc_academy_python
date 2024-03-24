n = int(input("Please enter number between 0 and 20: "))
print("Enter number: ", n)

print(n, end=" ")
while n != 1:

    if n % 2 == 0:
        n = n / 2
        print("->", int(n), end=" ")
        continue

    else:
        n = n * 3 + 1
        print("->", int(n), end=" ")
        continue
