user_input = input("Enter a string: ")
rotate = int(input("Enter number to rotate by: "))
string = ""
for ch in user_input:
    unicode = ord(ch)
    if 97 <= unicode <= 122:
        unicode += rotate
        if unicode < 97:
            unicode = 123 - (97 - unicode)
        elif unicode > 122:
            unicode = 96 + (unicode - 122)
    elif 65 <= unicode <= 90:
        unicode += rotate
        if unicode < 65:
            unicode = 91 - (65 - unicode)
        elif unicode > 90:
            unicode = 64 + (unicode - 90)
    string += chr(unicode) + " "
print(string.rstrip())