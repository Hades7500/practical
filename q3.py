user_input = input("Enter a string: ").split(" ")
string = ""
for word in user_input:
    for ch in word:
        unicode = ord(ch)
        unicode += 13
        if unicode > 122:
            unicode = 96 + unicode - 122
        elif 90 < unicode < 97:
            unicode = 64 + unicode - 90
        string += chr(unicode)
    string += " "
print(string)