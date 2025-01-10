# Program to copy odd lines from one file to another
source_file = "Samplefile.txt"
target_file = "odd_file.txt"

# Open the source file and the target file
with open(source_file, 'r') as source, open(target_file, 'w') as target:
    for line_number, line in enumerate(source, start=1):  # Enumerate to get line numbers
        if line_number % 2 != 0:  # Check if the line number is odd
            target.write(line)  # Write the odd line to the target file

print(f"Odd lines have been copied from {source_file} to {target_file}.")
