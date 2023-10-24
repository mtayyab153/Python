def find_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def find_common_divisors(num1, num2):
    divisors_num1 = find_divisors(num1)
    divisors_num2 = find_divisors(num2)
    common_divisors = set(divisors_num1) & set(divisors_num2)
    return list(common_divisors)

    # num1 = int(input("Enter the first number: "))
    # num2 = int(input("Enter the second number: "))


num_list = input("Enter pair of value with a comma separator: ")
num1, num2 = [int(num) for num in num_list.split(",")]

common_divisors = find_common_divisors(num1, num2)

if common_divisors:
    print("Common Divisors are: ", end="")
    for num in common_divisors:
        print(num, end=",")
else:
    print("There are no common divisors between", num1, "and", num2)
