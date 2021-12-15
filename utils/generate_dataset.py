import os
from math import floor
from random import shuffle
from utils.read_image import read_image
import numpy as np

def generate_dataset(dataset_path, img_height, img_width):
    x_train = []
    y_train = []
    x_valid = []
    y_valid = []
    x_test = []
    y_test = []
    encode = lambda x: 0 if x == "sharp_shinned" else 1
    for directory in os.listdir(dataset_path):
        print(f"Generating dataset for {directory}...")
        files = os.listdir(os.path.join(dataset_path, directory))
        shuffle(files)
        num_files = len(files)
        training_size = floor(num_files * 0.7)
        valid_size = floor(num_files * 0.2)
        test_size = floor(num_files * 0.1) 
        for i in range(training_size): # training
            image_path = os.path.join(dataset_path, directory, files[i])
            image = read_image(image_path, img_height, img_width)
            x_train.append(image)
            y_train.append(encode(directory))
        for i in range(training_size, training_size + valid_size):
            image_path = os.path.join(dataset_path, directory, files[i])
            image = read_image(image_path, img_height, img_width)
            x_valid.append(image)
            y_valid.append(encode(directory))
        for i in range(training_size + valid_size, training_size + valid_size + test_size):
            image_path = os.path.join(dataset_path, directory, files[i])
            image = read_image(image_path, img_height, img_width)
            x_test.append(image)
            y_test.append(encode(directory))
    return np.array(x_train), np.array(y_train), np.array(x_valid), np.array(y_valid), np.array(x_test), np.array(y_test)