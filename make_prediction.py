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
    print(make_prediction('/home/jasemichael/Downloads/sharp-shinned.jpg'))
    print(make_prediction('/home/jasemichael/Downloads/red-tailed.jpg'))
    print(make_prediction('/home/jasemichael/Downloads/red-tailed2.jpg'))
    print(make_prediction('/home/jasemichael/Downloads/sharp-shinned2.jpg'))