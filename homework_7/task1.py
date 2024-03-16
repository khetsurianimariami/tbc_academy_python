n = int(input("Please enter number between 0 and 20: "))
print("Enter number: ", n)

zero_element = 0
first_element = 1

if n == 0:
    print(zero_element)

elif n == 1:
    print(zero_element, first_element)

else:
    print(zero_element, end=" ")
    i = 0
    while i < n:
        zero_element, first_element = first_element, first_element + zero_element
        print(zero_element, end=" ")
        i += 1
