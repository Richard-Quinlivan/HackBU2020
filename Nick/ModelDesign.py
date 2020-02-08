## Nick Pellegrino
## Model Design for ChatBot
## No need to run this file

import tensorflow as tf
import tflearn

class ModelDesign:
    # Set up training epochs and batch size here
    epochs = 1000
    batchSize = 8

    def getModel(x_len, y_len):
        # Make a model
        model = tflearn.input_data(shape=[None, x_len])
        # Add two 128 hidden layers with 20% dropout after both
        model = tflearn.fully_connected(model, 128)
        model = tflearn.dropout(model, 0.8)
        model = tflearn.fully_connected(model, 128)
        model = tflearn.dropout(model, 0.8)
        # Final layer has softmax over all of our tags (y_len)
        model = tflearn.fully_connected(model, y_len, activation='softmax')
        model = tflearn.regression(model)
        # Set up tensorboard to save data
        model = tflearn.DNN(model, tensorboard_dir="Model")
        # Return the model
        return model
