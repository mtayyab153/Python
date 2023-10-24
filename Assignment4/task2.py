# Exercise 2: Print the sum of the current number and the previous number.
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and
# previous number.


def current_and_previous_sum():
    previous = 0
    current = 0
    print("Printing current and previous number sum in a range(10)")
    for i in range(10):
        summation = previous + current
        # print(f"Current Number {current} Previous Number {previous} Sum {summation}")
        print(
            "Current Number ", current, " Previous Number ", previous, " Sum", summation
        )
        previous = current
        current += 1


current_and_previous_sum()
