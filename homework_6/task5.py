n = int(input(" Please enter number between 0 and 10: "))

if (n > 0) and (n < 10):
    i = 1
    while i <= n:

        j = 1
        while j < (9 - i + 1):
            print(" ", end=" ")
            j += 1

        k = i
        while k > 0:
            print(k, end=" ")
            k -= 1

        m = 0
        while m < (i + 1):
            print(m, end=" ")
            m += 1

        i += 1

        print()

else:
    print("Please enter number between 0 and 10! ")
