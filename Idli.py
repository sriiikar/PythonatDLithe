# Program to print the maximum number of idlis

T = int(input("Enter the number of test cases: "))
a=[]
for i in range (0,T):
    A,B,K = map(int,input().split())
    x = K//A
    y = K//B
    z = max(x,y)
    a.append(z) # a is a list

for b in a:
    print(b) # printing each element of list a separately