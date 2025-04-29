import os 

import shutil 

from google.colab import drive 

  

drive.mount('/content/drive') 

  

dataset_path = '/content/drive/MyDrive/dataset' 

  

splits = ['test', 'train', 'valid'] 

  

suits = ['clubs', 'diamonds', 'hearts', 'spades'] 

  

for split in splits: 

    split_path = os.path.join(dataset_path, split) 

     

    for suit in suits: 

        os.makedirs(os.path.join(split_path, suit), exist_ok=True) 

     

    for class_folder in os.listdir(split_path): 

        if class_folder in suits: 

            continue 

             

        folder_path = os.path.join(split_path, class_folder) 

         

        if os.path.isdir(folder_path): 

            try: 

                suit = class_folder.split('of ')[-1].strip().lower() 

                if suit not in suits: 

                    print(f"jump joker: {class_folder}") 

                    continue 

                dest_path = os.path.join(split_path, suit) 

                for file_name in os.listdir(folder_path): 

                    src = os.path.join(folder_path, file_name) 

                    dst = os.path.join(dest_path, file_name) 

                    if os.path.exists(dst): 

                        base, ext = os.path.splitext(file_name) 

                        new_name = f"{base}_{class_folder}{ext}" 

                        dst = os.path.join(dest_path, new_name) 

                     

                    shutil.move(src, dst) 

                os.rmdir(folder_path) 

                 

            except Exception as e: 

                print(f"Error {class_folder} from: {str(e)}") 

  

print("complete！") 