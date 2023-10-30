# Loli-classification
Using a convolutional neural network to classify loli's, because why not.

This model (R.O.Y) was trained on 3000 images of anime faces that were resized to 80x80 pixels

Each image was labelled either 0 (loli) or 1 (non-loli)

The validation data was a set of 300 images while the final data (ds_final) was a set of 16 faces I wanted to try the model on

The training accuracy for the saved model is 91.77% while the test accuracy is 83.67%


Example of predictions on test set:
![Test predictions](https://github.com/JDurriher/Loli-classification/assets/54914481/4802aefd-1786-4473-b62a-80ba43eb3544)


The final test set of 16 images performed as below:
![1_C C](https://github.com/JDurriher/Loli-classification/assets/54914481/2c0f5e4a-9c5c-4c97-adcd-c8b9ee18bbeb)
![2_Riko](https://github.com/JDurriher/Loli-classification/assets/54914481/fee1a0a3-a782-4d67-b491-0d96605cf8c4)
![3_Makise Kurisu](https://github.com/JDurriher/Loli-classification/assets/54914481/ce4267ce-f9f8-48f2-8320-297c447448dd)
![4_Clannad girl](https://github.com/JDurriher/Loli-classification/assets/54914481/b46b91bf-1a98-4d2e-9dcc-0a94d8cf5136)
![5_Haysaka](https://github.com/JDurriher/Loli-classification/assets/54914481/91ae68d3-2883-44a6-9ce2-af139f8e5dfa)
![6_Anya](https://github.com/JDurriher/Loli-classification/assets/54914481/0a721368-31dc-4acf-b091-96983d5e42e6)
![7_Ed](https://github.com/JDurriher/Loli-classification/assets/54914481/8fe4fb18-526c-434f-b24a-0f0cb8a2e47d)
![8_Armin](https://github.com/JDurriher/Loli-classification/assets/54914481/590b8c54-c175-4081-a9c1-40495437056e)
![9_Gintama girl](https://github.com/JDurriher/Loli-classification/assets/54914481/2186abb0-fb8f-42f3-9c61-e3fffa0ab35e)
![10_Nezuko](https://github.com/JDurriher/Loli-classification/assets/54914481/6c1f4b8c-7ef0-4075-840f-e6b156015ff8)
![11_Mai](https://github.com/JDurriher/Loli-classification/assets/54914481/2cf4d0fa-e4c1-4056-b7c2-bda0e57db8d8)
![12_Hachikuji](https://github.com/JDurriher/Loli-classification/assets/54914481/9b27acfd-a409-4f40-a136-d73505b646b9)
![13_JJK Woman](https://github.com/JDurriher/Loli-classification/assets/54914481/2c281ef7-767a-4565-8f05-4e5b3d75ced1)
![14_Rem](https://github.com/JDurriher/Loli-classification/assets/54914481/8cad5c59-4f7c-412c-a6ab-609b9b581c5e)
![15_Senjougahara](https://github.com/JDurriher/Loli-classification/assets/54914481/ec6e927d-df1a-479f-91e3-dac82bddb4f2)
![16_Tatsumaki](https://github.com/JDurriher/Loli-classification/assets/54914481/f15dc038-aff7-4427-9084-423e8b407498)


If you want to retrain the model with your own dataset, in main.py replace the path for the training/testing/final directory with wherever your training images (anime faces) are stored

And then change the number at the end of line 28 to the number of directories you need to go through to get to the image file

Currently it's 8 but this likely won't be correct for you
