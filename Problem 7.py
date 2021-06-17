sent = input("Enter the sentence: ")

s1 = sent.split()
s2 = reversed(s1)
s3 = " ".join(s2)
print(s3)