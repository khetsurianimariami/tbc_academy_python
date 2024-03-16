n = int(input("Please enter number between 0 and 10000: "))
print("Enter number: ", n)

if (n >= 0) and (n < 10):
    print("Reversed number is: ", n)
    print("Sum of digits: ", n)

elif (n >= 10) and (n < 100):
    i = 0
    while i < 10:
        j = 0
        while j < 10:
            if (i * 10 + j) == n:
                print("Reversed number is: ", j, i, sep="")
                print("Sum of digits: ", j + i)
                break

            j += 1

        i += 1

elif (n >= 100) and (n < 1000):
    i = 0
    while i < 10:
        j = 0
        while j < 10:
            k = 0
            while k < 10:
                if (i * 100 + j * 10 + k) == n:
                    print("Reversed number is: ", k, j, i, sep="")
                    print("Sum of digits: ", k + j + i)
                    break

                k += 1

            j += 1

        i += 1

elif (n >= 1000) and (n < 10000):
    i = 0
    while i < 10:
        j = 0
        while j < 10:
            k = 0
            while k < 10:
                m = 0
                while m < 10:
                    if (i * 1000 + j * 100 + k * 10 + m) == n:
                        print("Reversed number is: ", m, k, j, i, sep="")
                        print("Sum of digits: ", m + k + j + i)
                        break

                    m += 1

                k += 1

            j += 1

        i += 1

else:
    print("Please enter number between 0 and 10000: ")
