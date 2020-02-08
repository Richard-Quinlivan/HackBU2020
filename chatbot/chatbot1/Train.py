## Nick Pellegrino
## ChatBot Trainer (uses ModelDesign.py)
## Run this file directly to train the ChatBot
## Saves training data to the Model folder

import json
import nltk
from nltk.stem.lancaster import LancasterStemmer
import random
import tflearn
import tensorflow as tf
import numpy as np
import pickle

from ModelDesign import ModelDesign

def loadData():
    with open('Training/trainingData.json', 'rb') as json_data:
        data = json.load(json_data)

    tags = []
    words = []
    combos = []

    for line in data['data']:
        for inputSentence in line['inputSentences']:
            # Tokenize words
            newWords = nltk.word_tokenize(inputSentence)
            # Add to word list and combo list
            words.extend(newWords)
            combos.append((newWords, line['tag']))
            # Add tag to tag list if it's new
            if line['tag'] not in tags:
                tags.append(line['tag'])

    # Stem, Lowercase, and Remove Duplicates in word data
    stemmer = LancasterStemmer()
    words = [stemmer.stem(w.lower()) for w in words]
    words = sorted(list(set(words)))

    # Remove Duplicates
    tags = sorted(list(set(tags)))

    return(tags, words, combos)

def convertData(tags, words, combos):
    training = []
    output = []
    output_empty = [0] * len(tags)

    for c in combos:
        # Stem words
        stemmer = LancasterStemmer()
        tokenWords = [stemmer.stem(w.lower()) for w in c[0]]

        # Create BagOfWords Array
        bagOfWords = []
        for w in words:
            bagOfWords.append(1) if w in tokenWords else bagOfWords.append(0)

        # Output layer (one-hot encode to the correct tag)
        output_layer = list(output_empty)
        output_layer[tags.index(c[1])] = 1

        # Add to training list (input layer is bag of words array)
        training.append([bagOfWords, output_layer])

    # Shuffle features and convert to numpy array
    random.shuffle(training)
    training = np.array(training)

    return list(training[:,0]), list(training[:,1])

def buildModel(train_x, train_y):
    # Reset graph
    tf.reset_default_graph()

    # Load model
    model = ModelDesign.getModel(len(train_x[0]), len(train_y[0]))

    # Tensorflow train
    model.fit(train_x, train_y, n_epoch = ModelDesign.epochs, batch_size = ModelDesign.batchSize, show_metric = True)

    # Save model
    model.save('Model/model.tflearn')

def train():
    # Load data
    tags, words, combos = loadData()

    # Convert data to tensors
    train_x, train_y = convertData(tags, words, combos)

    # Build model
    buildModel(train_x, train_y)

    # Save data
    pickle.dump({'tags':tags, 'words':words, 'train_x':train_x, 'train_y':train_y}, open('Model/data.pickle', 'wb'))

def main():
    print("Loading...")
    train()
    print("Done!")

if __name__ == '__main__':
    main()
