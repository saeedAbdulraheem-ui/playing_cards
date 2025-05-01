# 🃏 Playing Cards Classification & Application Suite

This repository contains various scripts and data used for building, training, deploying, and running a playing card classification system using Edge Impulse, TensorFlow Lite, and OpenMV.

---

## 📂 Files Overview

### 🔧 Data Preparation & Training
- **`Augmented_files_dataextraction.ipynb`**  
  Notebook for:
  - Augmenting training data for the 4-suit classification model.
  - Extracting log info from Edge Impulse to generate accuracy graphs seen in Figure 5 of report.

- **`86percent53class.ipynb`**  
  TensorFlow model notebook for classifying 53 playing card classes. Includes:
  - Training pipeline.
  - Model quantization.
  - `.tflite` model generation.

- **`changedataset.py`**  
  Script to reorganize a 53-class dataset into 4 suit categories.

---

### 🤖 Model & Deployment
- **`playing_card_model_micro.tflite`**  
  TensorFlow Lite model trained on 53-class playing card dataset — ready for deployment.

- **`ei-task2_image_classification-openmv-v10.zip`**  
  Contains:
  - Classification labels.
  - OpenMV script.
  - TFLite model deployed on RT1062.

- **`ei-runweini-project-1-openmv-v7.zip`**  
  Codebase for OpenMV-based card sorting by suit.

---

### 🕹️ Applications
- **`ei_image_classification.py`**  
  OpenMV classification script for identifying 4 suits. Includes bounding box functionality.

- **`game_colour.py`**  
  Application to classify and score cards based on their color.

- **`game_score.py`**  
  Application to classify and score cards based on their suit.

- **`snapshot_edited.py`**  
  OpenMV script to capture images of cards by suit.

---

### 💡 Utilities
- **`serial_logger.py`**  
  Listens to OpenMV serial output and logs classification data.

- **`Storgelogfile.py`**  
  Stores a log file directly on the OpenMV camera during runtime.

- **`led_flash_prog.py`**  
  Controls LEDs on the OpenMV to flash patterns representing detected cards.

---

### 🗃️ Datasets
- **`new data.zip`**  
  Card images captured via OpenMV on RT1062 — *not used due to occlusion issues*.

- **`real_card_data.zip`**  
  Final dataset of card images captured using OpenMV RT1062 — *used for training and evaluation*.

  - **`renamed files - 4 suits`**  
  Dataset used for model training for Kaggle with augmented Kaggle files - too large to upload to GitHub but can be accessed on OneDrive via this link:
  https://ulcampus-my.sharepoint.com/:f:/r/personal/24228109_studentmail_ul_ie/Documents/renamed%20files%20-%204%20suits?csf=1&web=1&e=5ABfE4
  
  Folder structure:
    train, test, valid - original Kaggle data used to train and test model
    train_data, aug_data - train file split, 2009 files in aug_data for augmentation and remaining training files in train_data
    augment_data_2 - augmented data from Kaggle ( 1 augment  per file from aug_data)

---

### 📄 Logs
- **`logfile of classification with 4 suits.txt`**  
  Logfile containing log data on four suits from OpenMV IDE.

- **`logfile_edgeimpulse.txt`**  
  Log file containing data that was extracted from Edge impulse based on training data for default CNN, used to generate Figure 5 in report.
 
