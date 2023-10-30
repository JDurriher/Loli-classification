![10_Nezuko](https://github.com/JDurriher/Loli-classification/assets/54914481/5576d844-5a69-429a-a057-55cbed255d00)# Loli-classification
Using a convolutional neural network to classify loli's, because why not.

This model (R.O.Y) was trained on 3000 images of anime faces that were resized to 80x80 pixels

Each image was labelled either 0 (loli) or 1 (non-loli)

The validation data was a set of 300 images while the final data (ds_final) was a set of 16 faces I wanted to try the model on

The training accuracy for the saved model is 91.77% while the test accuracy is 83.67%
![Training history data](https://github.com/JDurriher/Loli-classification/assets/54914481/98c5c98a-d65b-43ad-b804-2a5143087f14)
![Training and validation history](https://github.com/JDurriher/Loli-classification/assets/54914481/ccea13a5-2b8a-453e-89b6-1cb793711b39)

Example of predictions on test set:
![Test predictions](https://github.com/JDurriher/Loli-classification/assets/54914481/b5048164-90ff-412b-b2c1-f887d93fdeff)

The final test set of 16 images performed as below:
![1_C C](https://github.com/JDurriher/Loli-classification/assets/54914481/edb219a5-c567-4eb1-b4af-4950f576cffb)
![2_Riko](https://github.com/JDurriher/Loli-classification/assets/54914481/1ace7298-a61d-4d67-8569-d2314dc0d852)
![3_Makise Kurisu](https://github.com/JDurriher/Loli-classification/assets/54914481/789eb805-0d6a-4afa-8721-3eb98d2b399e)
![4_Clannad girl](https://github.com/JDurriher/Loli-classification/assets/54914481/b6843f66-b47d-4115-b7c2-30d67655317a)
![5_Haysaka](https://github.com/JDurriher/Loli-classification/assets/54914481/a50f6d82-b3d0-4c54-8266-22d39d0ba5da)
![6_Anya](https://github.com/JDurriher/Loli-classification/assets/54914481/64639cd7-32f1-43ed-a0cf-ffe6ac3a0061)
![7_Ed](https://github.com/JDurriher/Loli-classification/assets/54914481/215eada6-86a3-4a79-b10d-9b1c4fb0079f)
![8_Armin](https://github.com/JDurriher/Loli-classification/assets/54914481/72980fd5-43fb-4d42-9681-5c33cc02156a)
![9_Gintama girl](https://github.com/JDurriher/Loli-classification/assets/54914481/5d8de710-67e0-46b7-895b-cbb05084d371)
![10_Nezuko](https://github.com/JDurriher/Loli-classification/assets/54914481/f7d88eed-abe0-4e47-ab64-a529179712d3)
![11_Mai](https://github.com/JDurriher/Loli-classification/assets/54914481/ba7039dd-b5d3-4c22-a383-32b213f3aa34)
![12_Hachikuji](https://github.com/JDurriher/Loli-classification/assets/54914481/a68f7cbe-02ad-42b0-b67a-3574ac172adf)
![13_JJK Woman](https://github.com/JDurriher/Loli-classification/assets/54914481/da27c719-c12e-412a-96c0-453d53ef160a)
![14_Rem](https://github.com/JDurriher/Loli-classification/assets/54914481/6a52e53f-e6ad-4f56-bb12-d6c48eea4518)
![15_Senjougahara](https://github.com/JDurriher/Loli-classification/assets/54914481/6fa52df5-218e-439e-b637-7434412ff2de)
![16_Tatsumaki](https://github.com/JDurriher/Loli-classification/assets/54914481/ab25023c-e2ee-42c4-9d5b-ab1f87704838)

If you want to retrain the model with your own dataset, in main.py replace the path for the training/testing/final directory with wherever your training images (anime faces) are stored

And then change the number at the end of line 28 to the number of directories you need to go through to get to the image file

Currently it's 8 but this likely won't be correct for you
