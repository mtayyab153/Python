number_list = [2, 3345, 5, 10, 20, 34]

# Approach 1:
# If the list is sorted in ascending order then we can find out the min and max easily i.e
# first number will be min and last number will be max.
# print("Min: ", number_list[0])
# print("Max: ", number_list[-1])

# Approach 2:
# If the list is unsorted then we have to compare the elements in the list.We should have two
# pointers pointing to min and max and check if min is less than list[i] then update max to that
# element else update min to that element.


min = number_list[0]
max = number_list[0]

for num in number_list:
    if min > num:
        min = num
    else:
        max = num

# i = 0
# while i < len(number_list):
#     if min < number_list[i]:
#         max = number_list[i]
#     else:
#         min = number_list[i]
#     i += 1

print("Min: ", min)
print("Max: ", max)


def get_min_and_max(number_list):
    min_number = number_list[0]
    max_number = number_list[0]

    for num in number_list:
        if num < min_number:
            min_number = num
        elif num > max_number:
            max_number = num

    return min_number, max_number
