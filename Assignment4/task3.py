# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an
# even index number.

input_str = input("Please enter a string: ")
print(type(input_str))


i = 0
while i < len(input_str):
    print(f"'{input_str[i]}'", end=",")
    i += 2
