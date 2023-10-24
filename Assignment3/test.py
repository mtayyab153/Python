# Method 1: If the list is sorted in ascending order
def determine_min_and_max(number_list):
    minimum_num = number_list[0]
    maximum_num = number_list[-1]
    return minimum_num, maximum_num


# min_num, max_num = determine_min_and_max([1, 2, 0, 10, 20, 34])


# print("Min: ", min_num)
# print("Max: ", max_num)
#


# Method 2: If the list is unsorted
def get_min_and_max(number_list):
    minimum_num = number_list[0]
    maximum_num = number_list[0]
    for num in number_list:
        if minimum_num > num:
            minimum_num = num
        elif maximum_num < num:
            maximum_num = num

    return minimum_num, maximum_num


# min_num, max_num = get_min_and_max([2, 4355, 20, 0, 34, 12, 90, 345])
# print("Min: ", min_num)
# print("Max: ", max_num)


def log_even_and_odd(number_list):
    for num in number_list:
        if num % 2 == 0:
            print(num, " is even")
        else:
            print(num, " is odd")


log_even_and_odd([2, 4355, 20, 0, 34, 12, 90, 345, 1])
