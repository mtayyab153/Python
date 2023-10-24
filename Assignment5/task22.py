def count_values_frequency(dictionary):
    frequency = {}

    for value_list in dictionary.values():
        for value in value_list:
            frequency[value] = frequency.get(value, 0) + 1

    return frequency


original_dict = {
    1: ["gfg", "best", "geeks"],
    2: ["gfg", "CS"],
    3: ["best", "for", "CS"],
    4: ["test", "ide", "success"],
    5: ["gfg", "is", "best"],
}

frequency_dict = count_values_frequency(original_dict)
print("Values Frequency:", frequency_dict)
