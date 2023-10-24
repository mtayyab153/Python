def rotate_list_right(lst, k):
    for i in range(0, k):
        temp = lst[len(lst) - 1]
        for j in range(len(lst) - 1, 0, -1):
            lst[j] = lst[j - 1]
        lst[0] = temp

    return lst


def rotate_list_left(lst, k):
    for i in range(0, k):
        temp = lst[0]
        for j in range(0, len(lst) - 1):
            lst[j] = lst[j + 1]
        lst[len(lst) - 1] = temp

    return lst


print(rotate_list_right([1, 2, 3, 4, 5], 2))
print(rotate_list_left([1, 2, 3, 4, 5], 2))
