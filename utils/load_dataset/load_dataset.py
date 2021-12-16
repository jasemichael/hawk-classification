import os
from math import floor
from random import shuffle

import numpy as np

from utils.load_dataset.read_image import read_image

def load_dataset(dataset_path, img_height, img_width):
    x_train = []
    y_train = []
    x_valid = []
    y_valid = []
    x_test = []
    y_test = []
    encode = lambda x: 0 if x == "sharp_shinned" else 1
    for bird_dir in os.listdir(dataset_path):
        for site_dir in os.listdir(os.path.join(dataset_path, bird_dir)):
            print(f"Loading dataset from {bird_dir} {site_dir}...")
            files = os.listdir(os.path.join(dataset_path, bird_dir, site_dir))
            shuffle(files)
            num_files = len(files)
            training_size = floor(num_files * 0.7)
            valid_size = floor(num_files * 0.2)
            test_size = floor(num_files * 0.1) 
            for i in range(training_size): # training
                image_path = os.path.join(dataset_path, bird_dir, site_dir, files[i])
                image = read_image(image_path, img_height, img_width)
                x_train.append(image)
                y_train.append(encode(bird_dir))
            for i in range(training_size, training_size + valid_size):
                image_path = os.path.join(dataset_path, bird_dir, site_dir, files[i])
                image = read_image(image_path, img_height, img_width)
                x_valid.append(image)
                y_valid.append(encode(bird_dir))
            for i in range(training_size + valid_size, training_size + valid_size + test_size):
                image_path = os.path.join(dataset_path, bird_dir, site_dir, files[i])
                image = read_image(image_path, img_height, img_width)
                x_test.append(image)
                y_test.append(encode(bird_dir))
    return np.array(x_train), np.array(y_train), np.array(x_valid), np.array(y_valid), np.array(x_test), np.array(y_test)