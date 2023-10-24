def int_to_word(num):
    # Dictionary for numbers up to 19
    num_to_word_dict = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
    }

    # Dictionary for tens multiples
    tens_to_word_dict = {
        2: "Twenty",
        3: "Thirty",
        4: "Forty",
        5: "Fifty",
        6: "Sixty",
        7: "Seventy",
        8: "Eighty",
        9: "Ninety",
    }

    if num < 20:
        return num_to_word_dict[num]

    elif num < 100:
        tens = num // 10
        ones = num % 10
        return tens_to_word_dict[tens] + (
            "" if ones == 0 else " " + num_to_word_dict[ones]
        )

    elif num < 1000:
        hundreds = num // 100
        remainder = num % 100
        return (
            num_to_word_dict[hundreds]
            + " hundred"
            + ("" if remainder == 0 else " and " + int_to_word(remainder))
        )

    elif num < 10000:
        thousands = num // 1000
        remainder = num % 1000
        return (
            num_to_word_dict[thousands]
            + " thousand"
            + ("" if remainder == 0 else " " + int_to_word(remainder))
        )

    else:
        return "Number out of range"


number = 30
word_representation = int_to_word(number)
print(f"{number} -> {word_representation}")
