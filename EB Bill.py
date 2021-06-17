# Program to calculate EB Bill

n = float(input("Enter the number of units: "))

if(n>=0 and n<=30):
    cost = 3.75
elif(n>=31 and n<100):
    cost = 5.2
elif(n>=101 and n<=200):
    cost = 6.75
else:
    cost = 7.8

total = n*cost
fixed = 60
tax = 0.05*(total+fixed)
grand_total = total+fixed+tax

print("Number of units used= ",n)
print("Cost for",n,"units= ",round(total,3))
print("Monthly fixed charges= ",round(fixed,3))
print("Tax= ",round(tax,3))
print("Total bill amount= ",round(grand_total,3))