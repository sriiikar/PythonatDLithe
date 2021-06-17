s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

a = len(s1)
b = len(s2)

for i in range(b-a+1):
    for j in range(a):
        if s2[i+j] != s1[j]:
            break

if j+1 == a:
    print("No")
else:
    print("Yes")