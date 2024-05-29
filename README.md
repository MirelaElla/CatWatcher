# CatWatcher
My Machine Learning Project

* Create dataset with "CreateDataset.ipynb". This script moves images around based on the labels found in the "labels.csv" file. This script is run only once.

* Remove duplicates or near-duplicates with "RemoveDuplicates.py" (see also https://pypi.org/project/ImageHash/). This script removes more than half of the images. The remaining images are further manually reviewed and corrected if necessary (e.g., incorrect labels). This script is run only once. (In the future I will do this step BEFORE labelling over 70'000 images *sigh*)

* Rename file names with "RenameFiels.py". Before training the model I want to rename the filenames to not have any hints in the names. This is done with the script "RenameFiles.py". This script is run only once.

* Handle imbalanced dataset (not yet implemented).

* Train model. # CatWatcher

* Model0 (Y version) deployed on 25/05/2024 (see bouncer Repo)
* More training data added. Data cleaned (duplicates removed). We now have a curated dataset. Same model trained on new dataset.
* Model1 (Y version) deployed on 29/05/2024 (see bouncer Repo). 
