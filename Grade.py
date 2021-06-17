# Program to calculate grade of a student

score = float(input("Enter the score: "))

if(score>=90 and score<=100):
    print("Grade O")
elif(score>=80 and score<90):
    print("Grade A+")
elif(score>=70 and score<80):
    print("Grade A")
elif(score>=60 and score<70):
    print("Grade B+")
elif(score>=50 and score<60):
    print("Grade B")
elif(score<50 and score>=0):
    print("No Grade")
else:
    print("Invalid Score")