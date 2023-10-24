# Exercise 1: Calculate the multiplication and sum of two numbers.
# Given two integer numbers return their product only if the product is equal to or lower than 1000,
# else return their sum.


def calculate_sum_and_product(number1, number2):
    summation = number1 + number2
    product = number1 * number2

    if product <= 1000:
        return product
    else:
        return summation

    # return product if product <= 1000 else summation


result1 = calculate_sum_and_product(20, 30)
result2 = calculate_sum_and_product(40, 30)
print("The result is ", result1)
print("The result is ", result2)
