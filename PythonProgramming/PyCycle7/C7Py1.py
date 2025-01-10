# Program to read a file line by line and store it in a list without '\n'
file_name = "pg1_file.txt"

# Open the file and read lines
with open(file_name, 'r') as file:
    lines_list = [line.strip() for line in file]  # Strips '\n' from each line

print("Lines stored in the list:")
print(lines_list)
