input_str = "I am A Test string"

i = 0
while i < len(input_str):
    if input_str[i] >= chr(97) and input_str <= chr(122):
        print(input_str[i])
    i += 1
