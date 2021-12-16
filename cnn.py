import tensorflow as tf
import pathlib
import matplotlib.pyplot as plt
import os

from utils.load_dataset.load_dataset import load_dataset

IMG_WIDTH = 75
IMG_HEIGHT = 75

CURRENT_DIR = str(pathlib.Path().resolve())
DATASET_DIR = os.path.join(CURRENT_DIR, 'dataset')

# Preprocessing
x_train, y_train, x_valid, y_valid, x_test, y_test = load_dataset(DATASET_DIR, IMG_HEIGHT, IMG_WIDTH)
assert len(x_train) != len(x_valid) and len(x_valid) != len(x_test)

# Model definition
model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
  tf.keras.layers.MaxPool2D(pool_size=(2, 2)),
  tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu'),
  tf.keras.layers.MaxPool2D(pool_size=(2, 2)),
  tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu'),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(64, activation='relu'),
  tf.keras.layers.Dense(2, activation='softmax')
])

# Training
model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.001, momentum=0.9),
              loss='mean_squared_error',
              metrics=['accuracy'])

history = model.fit(x_train, y_train, validation_data=(x_valid, y_valid), batch_size=16, epochs=10, shuffle=True)

# Evaluation
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

test_loss, test_acc = model.evaluate(x_test,  y_test, verbose=2)

model.save('models/model')
#tf.keras.models.load_model('models/model')