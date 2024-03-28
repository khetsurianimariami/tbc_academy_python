text_1 = input("Please input string number 1: ")
text_2 = input("Please input string number 2: ")

print("Input: ")
print(text_1)
print(text_2)

answer = True

for c in text_2:
    if c not in text_1 or text_2.count(c) != text_1.count(c):
        answer = False
        break

if not answer:
    print("NO")
else:
    print("YES")
