from keras.layers import Dense, Dropout, Conv2D, Flatten, MaxPooling2D
from keras.models import Model
from keras.callbacks import ModelCheckpoint
import numpy as np


class MyModel(Model):
    def __init__(self):
        super().__init__()
        self.conv1 = Conv2D(2, kernel_size=(3, 3), input_shape=(3, 3), padding="same", activation="relu")
        self.conv2 = Conv2D(64, kernel_size=(3, 3), activation="relu", padding="same")
        self.conv3 = Conv2D(128, kernel_size=(3, 3), activation="relu", padding="same")
        self.conv4 = Conv2D(128, kernel_size=(3, 3), activation="relu", padding="same")
        self.flatten = Flatten()
        self.dense1 = Dense(128, activation="relu")
        self.dense2 = Dense(256, activation="relu")
        self.dense3 = Dense(1, activation="tanh")
        self.dropout = Dropout(0.2)
        self.max1 = MaxPooling2D(pool_size=(2, 2), padding="same")
        self.max2 = MaxPooling2D(pool_size=(2, 2), padding="same")
        self.max3 = MaxPooling2D(pool_size=(4, 4), padding="same")

    def call(self, inputs):
        x = self.conv1(inputs)
        x = self.conv2(x)
        x = self.max1(x)
        x = self.conv3(x)
        x = self.max2(x)
        x = self.conv4(x)
        x = self.max3(x)
        x = self.dropout(x)
        x = self.flatten(x)
        x = self.dense1(x)
        x = self.dense2(x)
        output = self.dense3(x)
        return output