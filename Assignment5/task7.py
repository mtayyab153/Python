user_input = input("Enter comma separated values: ")

num_list = [int(num) for num in user_input.split(",")]

for num in num_list:
    print("*" * num)
