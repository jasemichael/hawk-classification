import tensorflow as tf
import numpy as np

from utils.load_dataset.read_image import read_image

def make_prediction(file_path):
    x_test = read_image(file_path, 75, 75)
    x_test = x_test.reshape(-1, 75, 75, 3)
    model = tf.keras.models.load_model('models/model')
    prediction = model(x_test, training=False)
    c = np.argmax(prediction, axis = 1)
    if c == [0]:
        answer = "Sharp-shinned"
    elif c == [1]:
        answer = "Red-tailed"
    return answer

if __name__ == "__main__":
    # change accordingly
    print(make_prediction('/home/jasemichael/Downloads/sharp-shinned3.jpg'))