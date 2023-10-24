summation = 0
count = 0

while True:
    num = int(input("Enter a number: "))
    count = count + 1
    if num < 0:
        break
    summation = summation + num

print("Count: ", count)
print("Summation", summation)

# summation = 0
# count = 0
# num = int(input("Enter a number: "))
# while num >= 0:
#     count = count + 1
#     summation = summation + num
#     num = int(input("Enter a number: "))
#
# print("Count: ", count)
# print("Summation: ", summation)
