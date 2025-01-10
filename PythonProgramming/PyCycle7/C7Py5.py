import csv

# Step 1: Create a dictionary
data = [
    {"Name": "Ajay", "Age": 21, "District": "Kannur"},
    {"Name": "Sujith", "Age": 21, "District": "Palakkad"},
    {"Name": "George", "Age": 22, "District": "Alappuzha"}
]

file_name = "output.csv"  # File to write and read

# Step 2: Write the dictionary to a CSV file
with open(file_name, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
    writer.writeheader()  # Write the header row
    writer.writerows(data)  # Write the data rows

print(f"Dictionary written to {file_name}.")

# Step 3: Read the CSV file and display its content
print("\nReading and displaying the CSV file content:")
with open(file_name, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
