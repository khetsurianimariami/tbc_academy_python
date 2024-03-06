n = int(input("Please enter number between 0 and 1000: "))

if (n > 0) and (n < 1000):
    print("Entered number = ", n)
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

else:
    print("Please enter number between 0 and 1000: ")














