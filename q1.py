def piglatin(word):

    vowels = "AEIOUaeiou"
    for i in range(len(word)):
        if word[i] in vowels:
            return word[i:] + word[0:i] + "ay" + " "
    return word

phrase = input("Enter phrase in english: ").split()
new_phrase = ""
for word in phrase:
    if word.isalpha():
        new_phrase += piglatin(word)
    else:
        new_phrase += word + " "

print(new_phrase.strip())