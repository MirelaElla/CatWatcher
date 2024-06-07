# CatWatcher

This repository contains scripts and models for training image data, which are labeled and sorted for various classification tasks. The models are organized as a cascade to achieve the goal of detecting when cats bring home prey.

This repository is closely related to the [bouncer](https://github.com/mesopotato/bouncer) repository, which handles model deployment on the Raspberry Pi. Images stored via the Raspberry Pi implementation in the bouncer repository are used here in CatWatcher to train models, which are subsequently utilized in bouncer, creating a circular workflow between the two repositories.

## Description of some Files

- **CreateDataset.ipynb**: Moves images based on labels found in the `labels.csv` file. This script is intended to be run once.
  
- **RemoveDuplicates.py**: Removes duplicates or near-duplicates using the [ImageHash](https://pypi.org/project/ImageHash/) library. This script significantly reduces the number of images and the remaining images are manually reviewed for accuracy. It is also intended to be run once. *(Note: In the future, this step will be done before labeling over 70,000 images)*.
  
- **RenameFiles.py**: Renames file names before model training.

- **RecreateLabels.py**: Recreates the labels after sorting images to different folders and renaming files. Also intended to be run once.

- **converter.py**: Converts Keras models to tensorflow lite models for deployment on Raspberry Pi, which requires smaller models

## Description of Cascading Models and Development/Deployment History

### Model for Detecting Approaching Cats (2 classes: approaching=1, not approaching=0)
- **Model0 (Y version)**:
  - Deployed on 25/05/2024 (see bouncer repo)
  - Additional training data added, duplicates removed, resulting in a curated dataset.
  - **Model1 (Y version)**: Trained on the new dataset.
    - Deployed on 29/05/2024 (see bouncer repo).

### Model for Classifying Our Cats (3 classes: Hali=0, Rex=1, Simba=2)
- **HRS3 Model**:
  - Deployed on 06/06/2024.
  - Bug fix applied on 07/06/2024 (see bouncer repo).

### Model for Detecting whether Simba brings Prey (2 classes: prey=1, no prey=0)
- coming soon

### Model for Generalized Prey Detection (2 classes: prey=1, no prey=0)
- coming soon


## Todos
- [x] Train Cat classification model (HRS)
- [x] Implement Cat classification model
- [ ] Move labeling procedure from deprecated CatDetector repo to CatWatcher repo
- [ ] Train Simba Prey model
- [ ] Implement Simba Prey model
- [ ] Collect more data for prey images of other cats
- [ ] Create a generalized prey detection model

### Improvements for Cat Approach Model
- [ ] Avoid resizing images to squares to prevent distortions
- [ ] Investigate keeping original camera frame proportions

### Improvements for Cat Classification Model
- [ ] Correct width/height mix-up to prevent distortions
- [ ] Address imbalanced dataset (Rex is underrepresented)
- [ ] Handle other animals (foreign cat, dog, fox, "Marder") - see examples/other

### Standardization
- [ ] Standardize image preprocessing for all models
  - [ ] Determine whether to use normalization layers in the model or normalization in preprocessing functions


