string = input("Enter a sentence: ").split()
rev_string = ""
for word in string:
    rev_string += word[::-1] + " "
print(rev_string.strip())