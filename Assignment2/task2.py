# print first and last sentence is th given string
# remove special characters from the string
# count characters in the given string
paragraph = "!Python, is a programming language. It is a powerful language.&@#$ We can also create web apps with it."


def log_first_and_last_sentence():
    split_paragraph = paragraph.split(".")
    first_sentence = split_paragraph[0]
    last_sentence = split_paragraph[-2]
    print(first_sentence)
    print(last_sentence)


def remove_special_chars(input_string):
    special_char_list = "[@#$%&^!]"
    for char in input_string:
        if char in special_char_list:
            input_string = input_string.replace(char, "")

    print(input_string)


def count_chars(input_str):
    char_count = {}
    for char in input_str:
        if char != " ":
            char_count[char] = char_count.get(char, 0) + 1

    most_common_char = max(char_count, key=char_count.get)
    print(f"'{most_common_char}' is appeared most in the paragraph.")


log_first_and_last_sentence()
remove_special_chars(paragraph)
count_chars(paragraph)
