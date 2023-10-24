def count_carry_operations(num1, num2):
    carry_count = 0  # Initialize the carry count to 0
    carry = 0  # Initialize the carry to 0

    while num1 > 0 or num2 > 0:
        digit_sum = (num1 % 10) + (num2 % 10) + carry

        if digit_sum >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0

        num1 //= 10
        num2 //= 10

    return carry_count


addition_problems = [(123, 456), (555, 555), (789, 123), (999, 1)]

for num1, num2 in addition_problems:
    carry_count = count_carry_operations(num1, num2)
    print(f"Carry operations for {num1} + {num2}: {carry_count}")
