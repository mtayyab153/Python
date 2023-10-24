def sort_list_of_tuples(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j][1] > lst[j + 1][1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


input_list = [("Alice", 25), ("Bob", 30), ("John", 18), ("Emma", 22)]
sort_list_of_tuples(input_list)
print(input_list)
