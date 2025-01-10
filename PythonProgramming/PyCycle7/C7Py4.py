import csv

# Program to read specific columns from a CSV file
file_name = "details.csv"
columns_to_read = [0, 2]  # (0 for first column, 2 for third column)

# Open the CSV file
with open(file_name, 'r') as csv_file:
    reader = csv.reader(csv_file)  # Create a CSV reader object
    for row in reader:
        selected_columns = [row[i] for i in columns_to_read]  # Select only the specified columns
        print(selected_columns)
