list1 = []
n = int(input("No.of elements: "))

for i in range(n):
    elt = int(input())
    list1.append(elt)

i = 1

if i < n:
    while i<n and list1[i] > list1[i-1]:
        i += 1
    while i<n and list1[i] == list1[i-1]:
        i += 1
    while i<n and list1[i] < list1[i-1]:
        i += 1
    print("Yes")
else:
    print("No")