N = int(input())

if N%2 == 0:
    print("Invalid")
else:
    for i in range(1,N+1):
        for j in range(1,N+1):
            if(i<=((N+1)/2)):
                if j == i:
                    print(j, end="")
                elif j == N + 1 - i:
                    print(j, end="")
                else:
                    print(" ", end="")
        print()