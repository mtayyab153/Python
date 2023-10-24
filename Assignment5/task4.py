file_name = "abc.java"

file_name = file_name.split(".")
# print(file_name)
print(file_name[-1])

# Method 2
# extension = ""
# i = 0
# idx = 0
# while i < len(file_name):
#     idx = i
#     if file_name[i] == ".":
#         extension = file_name[i + 1 :]
#         break
#     i += 1
#
# print(extension)
