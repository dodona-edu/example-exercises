import sys

source_file_path = sys.argv[1]
destination_file_path = sys.argv[2]

with open(source_file_path, 'r') as source_file:
    content = source_file.readlines()

content.sort()

with open(destination_file_path, 'w') as destination_file:
    destination_file.writelines(content)
