import csv

# Program to read rows from a CSV file and print as a list of strings
file_name = "details.csv"

# Open the CSV file
with open(file_name, 'r') as csv_file:
    reader = csv.reader(csv_file)  # Create a CSV reader object
    for row in reader:
        print(row)  # Each row is printed as a list of strings
