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

try:
    from chatbot2.ModelDesign import ModelDesign
except:
    from ModelDesign import ModelDesign

class ChatBot2:
    def __init__(self):
        # Error threshold (we throw out tags under this percentage)
        self.ERROR_THRESHOLD = 0
        # Load data from pickle and json files
        self.tags, self.words, self.train_x, self.train_y, self.trainingData = self.loadData()
        # Load model
        self.model = self.loadModel(len(self.train_x[0]), len(self.train_y[0]))

    def loadData(self):
        # Load pickle and json file data
        try:
            data = pickle.load(open('chatbot/chatbot2/Model/data.pickle', 'rb'))
            with open('chatbot/chatbot2/Training/trainingData.json', 'rb') as json_data:
                trainingData = json.load(json_data)
        except:
            try:
                data = pickle.load(open('chatbot2/Model/data.pickle', 'rb'))
                with open('chatbot2/Training/trainingData.json', 'rb') as json_data:
                    trainingData = json.load(json_data)
            except:
                data = pickle.load(open('Model/data.pickle', 'rb'))
                with open('Training/trainingData.json', 'rb') as json_data:
                    trainingData = json.load(json_data)
        # Return pickle and json file data
        return data['tags'], data['words'], data['train_x'], data['train_y'], trainingData

    def loadModel(self, lenX, lenY):
        # Reset graph
        tf.reset_default_graph()

        # Load model
        model = ModelDesign.getModel(lenX, lenY)
        try:
            model.load('chatbot/chatbot2/Model/model.tflearn'')
        except:
            try:
                model.load('chatbot2/Model/model.tflearn')
            except:
                model.load('Model/model.tflearn')

        return model

    def cleanUpSentence(self, sentence):
        # Tokenize sentence into word bits
        sentence_words = nltk.word_tokenize(sentence)
        # Stem & Lowercase each token
        stemmer = LancasterStemmer()
        sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
        return sentence_words

    def bagOfWords(self, inputSentence, words):
        # Tokenize
        sentence_words = self.cleanUpSentence(inputSentence)
        # Bag Of Words
        bagOfWords = [0]*len(words)
        for s in sentence_words:
            for index,word in enumerate(words):
                if word == s:
                    bagOfWords[index] = 1
        return np.array(bagOfWords)

    def classify(self, inputSentence):
        results = self.model.predict([self.bagOfWords(inputSentence, self.words)])[0]
        # Filter out predictions below the error threshold
        results = [[i,r] for i,r in enumerate(results) if r > self.ERROR_THRESHOLD]
        # Sort by probability
        results.sort(key=lambda x: x[1], reverse = True)
        return results # Return list

    def printResults(self, inputSentence):
        results = self.classify(inputSentence)
        for r in results:
            print("Tag: ", self.tags[r[0]].upper(), "\tCertainty: ", str(r[1]))
