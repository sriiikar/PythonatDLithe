n = int(input())
a = map(int, input().split())
a = list(set(list(a)))
l = len(a)
a = sorted(a)
print(a[l-2])