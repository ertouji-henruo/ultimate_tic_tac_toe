import numpy
from keras.layers import Dense, Dropout, Conv2D, Flatten, MaxPooling2D
from keras.models import Model
from keras.callbacks import ModelCheckpoint
import numpy as np


class MyModel(Model):
    def __init__(self):
        super().__init__()
        self.conv1 = Conv2D(2, kernel_size=(3, 3), input_shape=(9, 9), padding="same", activation="relu")
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


# model = MyModel()
# board = np.zeros(9).reshape(3, 3)
# print(board, board.ndim)
# board2 = np.zeros(9).reshape(3, 3)
# board3 = np.zeros(9).reshape(3, 3)
# board4 = np.zeros(9).reshape(3, 3)
# board5 = np.zeros(9).reshape(3, 3)
# board6 = np.zeros(9).reshape(3, 3)
# board7 = np.zeros(9).reshape(3, 3)
# board8 = np.zeros(9).reshape(3, 3)
# board9 = np.zeros(9).reshape(3, 3)
# print(board.shape)
# test = [[board], [board2], [board3], [board4], [board5], [board6], [board7], [board8], [board9]]
# test = np.array(test)
# train = [[board]]
# train = np.array(train)
# validation = [[-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1]]
# validation = np.array(validation)
# model.compile(optimizer="adam", loss="mse",)
# model.fit(test, validation, batch_size=1, epochs=200)
