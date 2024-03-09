n = int(input("Please enter number between 0 and 20: "))
numerical_sequence = [0, 1]

if (n > 0) and (n < 20):
    print("Entered number = ", n)
    for i in range(0, 1000):
        numerical_sequence.append((numerical_sequence[i] + numerical_sequence[i + 1]))
    print(f"The {n}th term of the numerical sequence is {numerical_sequence[n]}")

else:
    print("Please enter number between 0 and 20: ")

