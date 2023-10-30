# Loli-classification
Using a convolutional neural network to classify loli's, because why not.

This model (R.O.Y) was trained on 3000 images of anime faces that were resized to 80x80 pixels

Each image was labelled either 0 (loli) or 1 (non-loli)

The validation data was a set of 300 images while the final data (ds_final) was a set of 16 faces I wanted to try the model on

The training accuracy for the saved model is 91.77% while the test accuracy is 83.67%
![Training history data](https://github.com/JDurriher/Loli-classification/assets/54914481/98c5c98a-d65b-43ad-b804-2a5143087f14)
![Training and validation history](https://github.com/JDurriher/Loli-classification/assets/54914481/ccea13a5-2b8a-453e-89b6-1cb793711b39)


Example of predictions on test set:


The final test set of 16 images performed as below:



If you want to retrain the model with your own dataset, in main.py replace the path for the training/testing/final directory with wherever your training images (anime faces) are stored

And then change the number at the end of line 28 to the number of directories you need to go through to get to the image file

Currently it's 8 but this likely won't be correct for you
