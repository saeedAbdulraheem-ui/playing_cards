# 🃏 Playing Cards Classification & Application Suite

This repository contains various scripts and data used for building, training, deploying, and running a playing card classification system using Edge Impulse, TensorFlow Lite, and OpenMV.

---

## 📂 Files Overview

### 🔧 Data Preparation & Training
- **`Augmented_files_dataextraction.ipynb`**  
  Notebook for:
  - Augmenting training data for the 4-suit classification model.
  - Extracting log info from Edge Impulse to generate accuracy graphs.

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

---

### 📄 Logs
- **`logfile of classification with 4 suits.txt`**  
 
