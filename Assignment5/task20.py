def concatenate_lists(lst):
    new_list = []
    i = 0
    while i < len(lst):
        new_list += lst[i]
        i += 1
    print(new_list)


concatenate_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
