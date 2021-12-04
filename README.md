# Image Augmentation Pipeline to increase dataset

## How to activate the file
1) cd into the file directory where ``Image_Augmentation.py`` is located
2) Create and activate a virtual environment. Here's a detailed [guide](https://towardsdatascience.com/virtual-environments-for-absolute-beginners-what-is-it-and-how-to-create-one-examples-a48da8982d4b) about virtual env's 
3) Do ``pip install -r requirements.txt``
4) Edit the Augmentation Pipeline based on your use case
5) Edit ``input_path`` and ``destination_path``
6) Edit file names in ``old_file_name`` and ``new_file_name``
7) Run ``Python Image_Augmentation.py`` 

## Suggestions for pipeline construction
I would highly suggest checking out the [official Albumentations documentation](https://albumentations.ai/docs/) to customise your pipeline. It is also suggested that you read up on relevant articles to understand what image augmentations works for your use case. Think of image augmentation as a way to enlarge your dataset by simulating different real life conditions. This technique may increase your ml model's performance, so do check out the official Albumentations documentation and read up on a variety of articles to get a proper understanding on image augmentations.
