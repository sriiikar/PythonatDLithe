sent = input("Enter the sentence: ")
s1 = sent.split()

for word in s1:
    if len(word) % 2 == 0:
        print(word)