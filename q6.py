def balanced(nums):
    odd = 0
    even = 0
    for num in nums:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    if even != odd:
        return False
    return True

nums = []

while True:
    list_input = input("Enter a number: ")
    if list_input.isdigit():
        nums += [int(list_input)]
    else:
        break

if balanced(nums):
    print("There is an equal number of odd and even numbers")
else:
    print("The number of odds and evens is not equal")
