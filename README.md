# Trash Sorting Project

This project is made to help the community to sort through Plastic and Metal waste.

Souce code can be find in venv -> main.py
Location of the datasets used can be seen on the "Contents" section below.

## Contents

The folder [Model](Model) contains trash image files that has been converted to Keras file. Trash images collected from Indonesia and from https://github.com/Patipol-BKK/alphatrash-dataset (Trash_dataset). The images has been taken using a Samsung Phone camera (Indonesia) and a Raspberry Pi Camera Module 2 [Patipol-BKK_Github].

The images of trash that are used in the dataset of this project is located at https://drive.google.com/drive/folders/1Wk489XjVThxPe7kJDf930I3DiVSV4CRs?usp=sharing
Note: plastic dataset images are not all used to train this AI Keras model.

The amount of images for each class is as follows:
Nothing (Contains the state where nothing is captured;      - 26
         may add some images to your prefered state of
         nothing)
Plastic (Contains plastic waste)                            - 2224 (images used to train the AI: 1050)
Metal   (Contains metal based waste)                        - 1138

## Training the AI

The AI is trained using Teachable Machine Website [https://teachablemachine.withgoogle.com/train/image], the trash Class is seperated to 3 different classes.
The 3 classes are Nothing, Plastic, Metal.

## Python Code

The python code is written using reference from Recyclable Waste Classifier using Opencv Python | Computer Vision by Murtaza's Workshop - Robotics and AI [https://youtu.be/EM9fA0uJn6w?si=voq76iaOLttF0cE7]. The code itself in this project is modified to fit the resources from this project.

The path in the code may be different, change the path to your path used to run this code.

## Contact Information

The project is made by a team of 3 people. Contact information for the people involved in this projects:
- darrenleonard777@gmail.com
- alvinrw04@gmail.com
- aufapasha321@gmail.com
