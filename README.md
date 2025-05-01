# playing_cards

###### Augmented_files_dataextraction.ipynb.ipynb - code to augment files that were used to train 4 suit model and code to extract log file info from edge impulse to make accuracy graphs
###### ei_image_classification.py - code to run classification on open mv ide for 4 suits (contains bounding box for classification)
###### ei-task2_image_classification-openmv-v10.zip - zip file containing labels, classification script and tflite model deployed on RT 1062
###### game_colour.py - application with classification, scores classified cards on colour
###### game_score.py - application with classification, scores classified cards based on suits
###### snapshot_edited.py - file to run on open mv ide to take pictures of cards based on suits
###### new data.zip - pictures taken of cards using RT 1062 in Open MV IDEe (not used due to too much occlusio)
###### real_card_data.zip - pictures taken of cards using RT 1062 in Open MV IDE (this data was used)
###### 86percent53class.ipynb - python notebook file containing tensorflow model trained on the playing card dataset (53 classes), additionally contains quantization and generation of .tflite model
###### playing_card_model_micro.tflite - 53 class playing card classification model in tensorflow lite format, ready for deployment
###### led_flash_prog.py - python program for openMV controller to flash LED's equivelant to detected card
###### ei-runweini-project-1-openmv-v7.zip Code for sorting playing cards by suit in OpenMV
###### serial_logger.py Code for listening on the OpenMV port to log a logfile
###### Storgelogfile.py Code that implements storing a logfile into the camera while it is running
###### changedataset.py Code that implements the reorganization of a dataset that originally classified playing cards into 53 categories into a classification by suit
###### logfile of classification with 4 suits.txt logfile of classification with 4 suits
