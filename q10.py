word_list = input("Enter a list of words: ").split()
word_dict = {}
for word in word_list:
    count = word_list.count(word)
    if (count in word_dict) and (word not in word_dict[count]):
        word_dict[count] += [word]
    else:
        word_dict[count] = [word]
print(word_dict)