import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pathlib
import matplotlib.pyplot as plt

img_height = img_width = 80
img_size = (img_height, img_width)
batch_size = 32

training_directory = 'Archions/ML/Loli Classification/training_3000'
testing_directory = 'Archions/ML/Loli Classification/test_300'
final_directory = 'Archions/ML/Loli Classification/tfinal_16'
ds_train = tf.data.Dataset.list_files(str(pathlib.Path(training_directory+'\\*.jpg')))
ds_test = tf.data.Dataset.list_files(str(pathlib.Path(testing_directory+'\\*.jpg')))
ds_final = tf.data.Dataset.list_files(str(pathlib.Path(final_directory+'\\*.jpg')))


def process_path(file_path):
    image = tf.io.read_file(file_path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, img_size)
    image = image / 255.0
    label = tf.strings.split(file_path, '\\')
    label = tf.strings.substr(label, pos=0, len=1)[8]
    label = tf.strings.to_number(label, out_type=tf.int64)
    return image, label


ds_train = ds_train.map(process_path).batch(batch_size)
ds_test = ds_test.map(process_path).batch(batch_size)
ds_final = ds_final.map(process_path).batch(batch_size)

# CNN model
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(ds_train, epochs=10, verbose=2, validation_data=ds_test)
model.evaluate(ds_final, verbose=2)

model.summary()
model.save('loli_classifier_model.keras')

# Visualizations:
# Display a few images from the test set and R.O.Y.'s predictions
images, labels = next(iter(ds_test))
predictions = model.predict(images)

plt.figure(figsize=(16, 16))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.imshow(images[i])
    prediction = "Loli" if predictions[i][0] < 0.5 else "Not Loli"
    actual = "Loli" if labels[i] == 0 else "Not Loli"
    plt.title(f'R.O.Y: {prediction}, Actual: {actual}')
    plt.axis('off')
plt.show()

images, labels = next(iter(ds_final))
predictions = model.predict(images)

# Display the final 16 characters and R.O.Y.'s predictions
for i in range(16):
    plt.figure(figsize=(6, 6))
    plt.imshow(images[i])

    currentPrediction = predictions[i][0]
    prediction = "Loli" if currentPrediction < 0.5 else "Not Loli"
    actual = "Loli" if labels[i] == 0 else "Not Loli"
    predictionConfidence = 1 - currentPrediction if currentPrediction < 0.5 else currentPrediction
    confidence_percentage = '{:.1%}'.format(predictionConfidence)

    plt.title(f'R.O.Y: {prediction}, Actual: {actual}')
    plt.text(0.5, -0.1, f'Confidence: {confidence_percentage}', transform=plt.gca().transAxes, fontsize=12, ha='center')
    plt.axis('off')
plt.show()
