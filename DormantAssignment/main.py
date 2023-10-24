import os
import re
import shutil

# read files from directory
path = "C://Users//PC1//PycharmProjects//DormantAssignment//Documents"
file_lst = os.listdir(path)
# print(file_lst)

cnic_pattern = r'\b(\d{5}-\d{7}-\d{1}|\d{13})\b'

file_dict = {}

file_paths = []


for file in file_lst:
    if file.endswith(".pdf"):
        match = re.search(cnic_pattern, file)
        if match:
            cnic = match.group(1).replace('-','')

            if cnic in file_dict:
                file_dict[cnic].append(file)
            else:
                file_dict[cnic] = [file]
        else:
            print(f"No CNIC found in '{file}'")
    else:
        print(f"Unable to process the file '{file}'")

print(file_dict)
# for key, value in file_dict.items():
#     print(key, value)

def move_file(filename):
    source = "C://Users//PC1//PycharmProjects//DormantAssignment//Documents//"
    destination = "C://Users//PC1//PycharmProjects//DormantAssignment//Not Processed//"
    src_path = os.path.join(source, filename)
    dst_path = os.path.join(destination, filename)
    shutil.move(src_path, dst_path)
    print(filename, "moved to Destination Directory.")

for key,value in file_dict.items():
    if len(value) == 1:
        move_file(str(value[0]))

