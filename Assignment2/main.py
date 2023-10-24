# # Task 1:
# # Print numbers from 1 to 20. Check if the number is even or odd. If even then show the smallest and largest number
# # in evens and do the same for odd.
even_list = []
odd_list = []
for i in range(1, 21):
    print(i)
    if i % 2 == 0:
        # print(f"{i} is Even")
        even_list.append(i)
    else:
        # print(f"{i} is Odd")
        odd_list.append(i)

print("Even List: ", even_list)
print("Odd List: ", odd_list)
print("Smallest Number in even list: ", even_list[0])
print("Largest Number in even list: ", even_list[-1])
print("Smallest Number in odd list: ", odd_list[0])
print("Largest Number in odd list: ", odd_list[-1])


# Task 1 Method-2:
# Print numbers from 1 to 20. Check if the number is even or odd. If even then show the smallest and largest number
# in evens and do the same for odd.
# even_list = [4, 2, 18, 40]
# odd_list = [1, 3, 9, 19]
#
#
# # smallest and largest number in evens
# i = 0
# smallest_even_num = even_list[0]
# largest_even_num = even_list[0]
# while i < len(odd_list):
#     if smallest_even_num > even_list[i]:
#         smallest_even_num = even_list[i]
#     else:
#         largest_even_num = even_list[i]
#     i += 1
# print("Smallest even: ", smallest_even_num)
# print("Largest even: ", largest_even_num)
#
#
# # smallest and largest number in odds
# i = 0
# smallest_odd_num = odd_list[0]
# largest_odd_num = odd_list[0]
# while i < len(odd_list):
#     if smallest_odd_num > odd_list[i]:
#         smallest_odd_num = odd_list[i]
#     else:
#         largest_odd_num = odd_list[i]
#     i += 1
# print("Smallest odd: ", smallest_odd_num)
# print("Largest odd: ", largest_odd_num)
