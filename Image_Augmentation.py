import albumentations as A
import cv2
import os
import shutil
from pathlib import Path

# Declare an augmentation pipeline, for more customisation options please look at the albumentations docs
transform = A.Compose([
    A.Sharpen (alpha=(0.2, 0.5), lightness=(0.2, 0.5), p=0.5),
    A.ToSepia (p=0.3),
    A.RandomToneCurve (scale=0.2, p=0.7),
])

# Change the file paths for input_path and destination_path to yours.
input_path = 'Images_Data/'
destination_path = 'Altered_Images/'
file_directory = Path(input_path)

if file_directory.exists():
  for dirpath, dirs, files in os.walk(input_path): 
    for filename in files:
      fname = os.path.join(dirpath,filename) 
      if fname.endswith('.jpg') or fname.endswith('.jpeg') or fname.endswith('.png'):  
        # Read an image with OpenCV
          image = cv2.imread(fname)
          input_path_extension = filename.split('.')[0]
          # Augment an image
          transformed = transform(image=image)
          transformed_image = transformed["image"]
          # Change file name here to your preference, output will be image1_sharpen_sepia_randomtone.jpg
          cv2.imwrite(destination_path + str(input_path_extension) + "_sharpen_sepia_randomtone" + ".jpg", transformed_image)
      elif fname.endswith('.txt'):
          input_path_extension = filename.split('.')[0]
          old_file_name = destination_path + input_path_extension + ".txt"
          new_file_name = destination_path + str(input_path_extension) + "_sharpen_sepia_randomtone" + ".txt"
          shutil.copyfile(input_path + input_path_extension + ".txt", old_file_name)
          os.rename(old_file_name, new_file_name)
else:
  raise Exception('The input filepath is not valid, please try again')