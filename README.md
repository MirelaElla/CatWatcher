# CatWatcher

This repository contains scripts and models for training image data, which are labeled and sorted for various classification tasks. The models are organized as a cascade to achieve the goal of detecting when cats bring home prey. Currently, we focus on our three cats: Hali, Rex, and Simba. In the future, we plan to develop a more generalizable model.

This repository is closely related to the [bouncer](https://github.com/mesopotato/bouncer) repository, which handles model deployment on the Raspberry Pi. Images stored via the Raspberry Pi implementation in the bouncer repository are used here in CatWatcher to train models, which are subsequently utilized in bouncer, creating a circular workflow between the two repositories.

## Description of Cascading Models and Development/Deployment History

### Model for Detecting Approaching Cats (2 classes: approaching=1, not approaching=0)
- **Model0 (Y version)**:
  - Deployed on 25/05/2024 (see bouncer repo)
  - Additional training data added, duplicates removed, resulting in a new dataset.
  - **Model1 (Y version)**: Trained on the new dataset.
    - Deployed on 29/05/2024 (see bouncer repo).
  - **Model2 (model_approach.tflite)**: Trained on the new dataset with new model architecture.
    - Deployed beginning of June 2024

### Model for Classifying Our Cats (3 classes: Hali=0, Rex=1, Simba=2)
- **HRS3 Model**:
  - Deployed on 06/06/2024.
  - Bug fix applied on 07/06/2024 (see bouncer repo).

### Model for Detecting whether Simba brings Prey (2 classes: prey=1, no prey=0)
- model_prey.h5/model_prey.tflite

### Model for Generalized Prey Detection (2 classes: prey=1, no prey=0)
- coming soon

## Description of some Helper Functions

- **CreateDataset.ipynb**: Moves images based on labels found in the `labels.csv` file. This script is intended to be run once.
  
- **RemoveDuplicates.py**: Removes duplicates or near-duplicates using the [ImageHash](https://pypi.org/project/ImageHash/) library. This script significantly reduces the number of images and the remaining images are manually reviewed for accuracy. It is also intended to be run once. *(Note: In the future, this step will be done before labeling over 70,000 images)*.
  
- **RenameFiles.py**: Renames file names before model training.

- **RecreateLabels.py**: Recreates the labels after sorting images to different folders and renaming files. Also intended to be run once.

- **converter.py**: Converts Keras models to TensorFlow Lite format, which is a more efficient format suitable for low-power devices like the Raspberry Pi

- **labelling/Labelling2.py**: Psychopy script for labelling images. This script was originally run in a different (deprecated) [repository](https://github.com/MirelaElla/CatDetector/tree/master/CatMouth)

## Todos
- [x] Add libraries to requirements.txt file (done but maybe still incomplete)
- [x] Train Cat classification model (HRS)
- [x] Implement Cat classification model
- [x] Move labeling procedure from deprecated CatDetector repo to CatWatcher repo
- [x] Train Simba Prey model (done but can be improved)
- [ ] Implement Simba Prey model
- [ ] Collect more data for prey images of Hali and Rex *(cuz they're no saints either)*
- [ ] Create a generalized prey detection model
    - [ ] Converting images to grayscale could be useful, as it allows us to use more diverse images.

### Improvements for Cat Approach Model
- [x] Avoid resizing images to squares to prevent distortions --> nah it is easier to handle quadratic images
- [x] Investigate keeping original camera frame proportions --> images are too big, model size gets too big for Raspberry Pi 3

### Improvements for Cat Classification Model
- [x] Correct width/height mix-up to prevent distortions --> made it quadratic
- [ ] Address imbalanced dataset (Rex is underrepresented)
- [ ] Handle other animals (foreign cat, dog, fox, "Marder") - see examples/other

### Standardization
- [ ] Standardize image preprocessing for all models
- [ ] Determine whether to use normalization layers in the model or normalization in preprocessing functions


