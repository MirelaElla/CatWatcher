import os
import csv

# Define the folder path
folder_path = 'cats_approach_training_2024_05_19'

# Define the output CSV file path
csv_file_path = 'labels2.csv'

# Initialize a list to store file names and their corresponding labels
file_labels = []

# Traverse the folder and subfolders
for subfolder in ['n', 'y']:
    subfolder_path = os.path.join(folder_path, subfolder)
    if os.path.exists(subfolder_path):
        for file_name in os.listdir(subfolder_path):
            if file_name.endswith('.jpg'):
                file_labels.append([file_name, subfolder])

# Write the list to a CSV file
with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the file names and labels
    csv_writer.writerows(file_labels)

print(f'CSV file {csv_file_path} created successfully.')
