n = int(input(" Please enter number between 0 and 10: "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    i += 1
    print(" ")

k = n - 1
while k > 0:
    m = 1
    while m < k + 1:
        print(m, end=" ")
        m += 1
    k -= 1
    print("\r")
