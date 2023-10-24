def check_all_alphabets(input_str):
    alphabet_string = "abcdefghijklmnopqrstuvwxyz"
    is_true = False
    for char in alphabet_string:
        if char in input_str:
            # print("hi")
            is_true = True
        else:
            print(char)
            is_true = False

    return is_true


print(check_all_alphabets("abcdefghijklmnopqrstuvwz"))


# input_str = "Ibc"
# alphabet_string = "abcdefghijklmnopqrstuvwxyz"


# for char in alphabet_string:
#     isTrue = False
#     if char in input_str:
#         print("hi")
#         isTrue = True
#     else:
#         print("nue")
#         isTrue = False
