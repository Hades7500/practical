def func(num_list):
    final_list = []
    for i in range(len(num_list)):
        if int(num_list[i]) % 2 == 0:
            sum = 0
            for digit in num_list[i]:
                sum += int(digit)
            final_list += [sum]
        else:
            product = 1
            for digit in num_list[i]:
                product *= int(digit)
            final_list += [product]
    return final_list

num_list = input("Enter a list of numbers: ").split()
print(func(num_list))