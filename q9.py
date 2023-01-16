def total(myDict): 
    sum = 0
    for num in myDict.values():
        sum += num

    return sum

num_of_items = int(input("Enter number of items: "))
num_dict = {}
for i in range(1, num_of_items + 1):
    num_dict[i] = int(input("Enter a number: "))
print("The sum of items in the dictionary is :", total(num_dict))