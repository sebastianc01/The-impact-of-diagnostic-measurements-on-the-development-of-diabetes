import pandas as pd
from sklearn import model_selection, datasets
from sklearn.tree import DecisionTreeClassifier
#import joblib
import pathlib
import string
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import tensorflow as tf

class NeuralNetwork:
    _model = tf.keras.models.Sequential()
    
    # load_model loads model from the exsiting file
    def load_model(self, filename: string):
        self._model = tf.keras.models.load_model(filename)
    
    # creates and trains model 
    def create_and_train_model(self, units: int, filename: string):
        dataset = pd.read_csv('diabetes.csv')
        x = dataset.drop(columns=["Outcome"])
        y = dataset["Outcome"]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.Dense(units, input_shape=x_train.shape[1:], activation=None))
        model.add(tf.keras.layers.Dense(2*units//3, activation='relu'))
        model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        #model.fit(x_train, y_train, epochs=400)
        #model.evaluate(x_test, y_test)
        history = model.fit(x=x_train, y=y_train, batch_size=64, epochs=500, validation_data=(x_test, y_test))
        # plt.plot(history.history['accuracy'])
        # plt.plot(history.history['val_accuracy'])
        # plt.title('model accuracy')
        # plt.ylabel('accuracy')
        # plt.xlabel('epoch')
        # plt.legend(['train', 'val'], loc='upper left')
        # plt.show()
        # plt.plot(history.history['loss'])
        # plt.plot(history.history['val_loss'])
        # plt.title('model loss')
        # plt.ylabel('loss')
        # plt.xlabel('epoch')
        # plt.legend(['train', 'val'], loc='upper left')
        # plt.show()
        tf.keras.models.save_model(model, filename)
        self._model = model
    
    # __init__ method, checks if the data is already trained, trains its otherwise
    def __init__(self, units: int, file: string):
        if pathlib.Path(file).exists():
            NeuralNetwork.load_model(self, file)
        else:
            self._model = NeuralNetwork.create_and_train_model(self, units, file)
    
    # returns already existing model
    def getModel(self):
        return self._model
