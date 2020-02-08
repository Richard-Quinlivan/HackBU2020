import keras
from keras.models import Sequential
from keras.optimizers import Adam
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dropout
from keras.layers import BatchNormalization
from keras.layers import Dense
from keras.layers import Flatten


import cv2
import glob
import numpy as np


class FaceDetectionNN():
    modelFile = "FaceDetectionModel.h5"
    def __init__(self):

        self.model = Sequential()

        self.model.add(Conv2D(32, activation='relu',padding='same',kernel_size=(3, 3),input_shape=(64,64,3)));
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(BatchNormalization())
        self.model.add(Dropout(0.2))

        self.model.add(Conv2D(64, activation='relu',padding='same',kernel_size=(3, 3)));
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(BatchNormalization())
        self.model.add(Dropout(0.2))

        self.model.add(Conv2D(128, activation='relu',padding='same',kernel_size=(3, 3)));
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(BatchNormalization())
        self.model.add(Dropout(0.2))

        self.model.add(Flatten())

        self.model.add(Dense(128, activation = 'relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(2, activation = 'sigmoid'))
        self.model.compile(loss='mse', optimizer=Adam(),metrics=['accuracy']);

    def train(self):
        imageArray = []
        labelArray = []

        bernie = glob.glob("./TrainImages/Bernie/*")
        trump = glob.glob("./TrainImages/Trump/*")

        for file in bernie:
            img = cv2.imread(file)
            img = cv2.resize(img, (64, 64),interpolation = cv2.INTER_AREA)

            imageArray.append(img)
            labelArray.append([1,0])

        for file in bernie:
            img = cv2.imread(file)
            img = cv2.resize(img, (64, 64),interpolation = cv2.INTER_AREA)

            imageArray.append(img)
            labelArray.append([0,1])

        imageArray = np.asarray(imageArray)
        labelArray = np.asarray(labelArray)

        print(imageArray.shape)
        print(labelArray.shape)
        print(labelArray)

        self.model.fit(imageArray, labelArray, epochs = 10)
        self.model.save(self.modelFile)

    def predict(self, img):
        predictionResult = self.model.predict(img)
        return predictionResult
