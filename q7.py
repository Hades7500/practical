number = int(input("Enter number of elements: "))
num_tuple = ()
for i in range(number):
    num = int(input("Enter a number: "))
    num_tuple += num,
print("The maximum value in the tuple is: ", max(num_tuple))
print("The minimum value in the tuple is: ", min(num_tuple))