import pandas as pd
from sklearn import model_selection, datasets
from sklearn.tree import DecisionTreeClassifier
#import joblib
import pathlib
import string
#import pickle
from sklearn.model_selection import train_test_split
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
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.Dense(units, input_shape=x_train.shape[1:], activation='sigmoid'))
        model.add(tf.keras.layers.Dense(units, activation='sigmoid'))
        model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        model.fit(x_train, y_train, epochs=1000)
        model.evaluate(x_test, y_test)
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

