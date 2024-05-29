import os
from PIL import Image
import imagehash

def remove_duplicates(directory):
    # Ensure the 'duplicates' folder exists
    duplicates_folder = os.path.join(directory, 'duplicates')
    if not os.path.exists(duplicates_folder):
        os.makedirs(duplicates_folder)

    # Dictionary to hold images and their hashes
    hashes = {}

    # Iterate through all image files in the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg')):
            # Create the full path to the file
            file_path = os.path.join(directory, filename)

            # Open the image and calculate its hash
            with Image.open(file_path) as img:
                img_hash = imagehash.average_hash(img)

            # If the hash is already in the dictionary, it's a duplicate
            if img_hash in hashes:
                # Generate a new path under the 'duplicates' folder
                dup_target_path = os.path.join(duplicates_folder, os.path.basename(file_path))
                os.rename(file_path, dup_target_path)  # Move the file
                print(f"Moved duplicate: {file_path} to {dup_target_path}")
            else:
                hashes[img_hash] = file_path  # Store the first occurrence

    print("Duplicate processing complete. Duplicates moved to the 'duplicates' folder.")

# Specify the path to your image directory
image_directory = 'C:/Users/mirela/Documents/gitRepos/CatWatcher/cats_approach_training_2024_05_19/y'
remove_duplicates(image_directory)