## Nick Pellegrino
## ChatBot (uses ModelDesign.py)
## No need to run this file directly

import json
import nltk
from nltk.stem.lancaster import LancasterStemmer
import random
import tflearn
import tensorflow as tf
import numpy as np
import pickle

from ModelDesign import ModelDesign

class ChatBot:
    def __init__(self):
        # Error threshold (we throw out tags under this percentage)
        self.ERROR_THRESHOLD = 0.25
        # Load data from pickle and json files
        self.tags, self.words, self.train_x, self.train_y, self.trainingData = self.loadData()
        # Load model
        self.model = self.loadModel(len(self.train_x[0]), len(self.train_y[0]))

    def loadData(self):
        # Load pickle and json file data
        data = pickle.load(open('Model/data.pickle', 'rb'))
        with open('Training/trainingData.json', rb) as json_data:
            trainingData = json.load(json_data)
        # Return pickle and json file data
        return data['tags'], data['words'], data['train_x'], data['train_y'], trainingData

    
