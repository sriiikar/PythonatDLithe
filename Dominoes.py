# Program to find maximum no.of dominoes

M,N = map(int, input().split())

if(M>=1 and M<=16):
    if(N>=1 and N<=16):
        area = M * N
        max = area // 2
        print(max)
else:
    print("Invalid Input")