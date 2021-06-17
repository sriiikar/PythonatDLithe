import re

string = input()

a = re.compile('[@_!#$%^&*()<>?/\|{}~:]')

if a.search(string) is None:
    print("String is accepted")
else:
    print("String is not accepted")