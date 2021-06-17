n=int(input(""))

if(n == 0):
    print("Neither Even nor Odd")
elif (n>0 and n<=100):
    if(n%2 != 0):
        print("Weird")
    elif(n>=2 and n<=5):
        print("Not Wieird")
    elif(n>=6 and n<=20):
        print("Weird")
    else:
        print("Not Weird")
else:
    print()