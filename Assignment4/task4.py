# Exercise 4: Remove first n characters from a string.
# Write a program to remove characters from a string starting from zero up to n and return a new string.


def remove_n_characters(str, n):
    new_str = str[n:]
    print(new_str)


remove_n_characters("pynative", 4)
remove_n_characters("pynative", 2)
