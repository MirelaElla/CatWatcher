import os
import pathlib

def clean_filenames(data_dir):
    # Traverse through all files in the directory and subdirectories
    for dirpath, dirnames, filenames in os.walk(data_dir):
        for filename in filenames:
            if "_cat" in filename:
                # Determine the new filename
                new_filename = filename.split("_cat")[0] + "_cat"
                new_filename += filename[filename.rfind('.'):]  # Append the file extension

                # Full path for old and new filenames
                old_file = os.path.join(dirpath, filename)
                new_file = os.path.join(dirpath, new_filename)

                # Rename the file
                os.rename(old_file, new_file)
                print(f"Renamed '{filename}' to '{new_filename}'")

# Specify the path to your data directory
data_dir = pathlib.Path('C:\\Users\\mirela\\Documents\\gitRepos\\CatWatcher\\cats_approach_training_2024_05_19')
clean_filenames(data_dir)
