n = int(input("Please enter number, between 0 and 50: "))

if (n > 0) and (n < 50):
    for i in range(1, n + 1):
        print(i, " - ", end=" ")
        c = 0
        for j in range(1, i + 1):
            if i % j == 0:
                c += 1
                print(j, end=" ", sep=" ")
            if c == 3:
                break
        print()

else:
    print("Please enter number, between 0 and 50: ")
