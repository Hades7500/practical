def search(num_list, num):
    for i in range(len(num_list)):
        if num == int(num_list[i]):
            return i
    return "Number not in list"

num_list = input("Enter a list of numbers: ").split()
num = int(input("Enter number to search for: "))
print(search(num_list, num))