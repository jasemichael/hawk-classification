import numpy as np
from PIL import Image

def read_image(image_path, img_height, img_width):
    image = np.array(Image.open(image_path))
    image = np.resize(image, (img_height, img_width, 3))
    image = image.astype('float32')
    image /= 255
    return image