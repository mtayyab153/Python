user_input = input("Enter comma separated values: ")

num_list = [int(num) for num in user_input.split(",")]

num_tuple = tuple(num_list)

print("List:", num_list)
print("Tuple", num_tuple)

# Method 1
# num_list = []
#
# num1 = 3
# num2 = 5
# num3 = 7
# num4 = 23
#
# num_list.append(num1)
# num_list.append(num2)
# num_list.append(num3)
# num_list.append(num4)
# print("List:", num_list, end="")

# Method 2:
# num_list = []
# for num in [3, 5, 7, 23]:
#     num_list.append(num)
# print("List:", num_list, end="")


# Method 3:
# nums_list = [3, 5, 7, 23]
# num_tuple = (3, 5, 7, 23)
#
# print("List:", nums_list, end="")
# print("Tuple:", num_tuple)
