def sort_num_descending_order(nums):
    size = len(nums)
    for i in range(size):
        for j in range(0, size - i - 1):
            if num_list[j] < num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]


nums = input("Enter values with space as a separator: ")
num_list = [int(num) for num in nums.split(" ")]

sort_num_descending_order(num_list)

for num in num_list:
    print(num, end=" ")
