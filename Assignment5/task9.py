# LCM
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    max_num = num1
else:
    max_num = num2

while True:
    if max_num % num1 == 0 and max_num % num2 == 0:
        break
    max_num += 1


print("LCM: ", max_num)
