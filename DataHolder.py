## Nick Pellegrino
## DataHolder holds data in a static way
## No need to run this file directly

from chatbot.CivicBot import CivicBot

# Importing Adi's face detection stuff
# from face_detection.FaceDetectionNN import FaceDetectionNN
# fd = FaceDetectionNN(False)

# Static class
class DataHolder:
    # Static variables
    convo = []
    first = "When it comes to politics, what's important to you? Feel free to speak candidly."
    bot = CivicBot()

    # Static methods
    @staticmethod
    def getSentence(sentence):
        return bot.getReply(sentence)
