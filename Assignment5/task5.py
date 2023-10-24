# def sort_without_conditionals_and_loops(lst):
#     for i in range(len(lst)):
#         for j in range(len(lst) - 1):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#
#     print(lst)
#
#
# sort_without_conditionals_and_loops([2, 3, 1, 8, 4, 45])


# def sort_without_conditionals_and_loops(a, b):
#     a = a + b
#     b = a - b
#     a = a - b
#     print(a, b)
#
#     # a = a * b
#     # b = a // b
#     # a = a // b
#     # print(a, b)
#
#
# sort_without_conditionals_and_loops(5, 4)


def sort_integers(a, b, c):
    minimum_value = min(a, b, c)
    maximum_value = max(a, b, c)
    mid_value = (a + b + c) - minimum_value - maximum_value

    return minimum_value, mid_value, maximum_value


print(sort_integers(10, 3, 19))
