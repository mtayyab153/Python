# Print table for integers.Create a dictionary having key = "str" for string, if there's one string then str="" , if
# multiple strings then str=['','','',....].
# Count true and false and set its count to a key in dict, igonore None.

data_list = [1, 2, 3, 4, 5, 6, 7, "aidf", "shjds", "tabassum", True, False, None
    , True, False, False]
isTrue = 0
isFalse = 0
str_list = []
data_dict = {}

for item in data_list:
    if type(item) == int:
        print(item)
    elif type(item) == str:
        str_list.append(item)
        print("str ", item)
    elif type(item) == bool:
        print("bool ", item)
        if item:
            isTrue += 1
        else:
            isFalse += 1
    else:
        print("value is not as per our requirements ", item)

if len(str_list) == 1:
    data_dict["str"] = str_list[0]
else:
    data_dict["str"] = str_list

data_dict["True"] = isTrue
data_dict["False"] = isFalse

print(data_dict)
