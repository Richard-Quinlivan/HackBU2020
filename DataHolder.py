## Nick Pellegrino
## DataHolder holds data in a static way
## No need to run this file directly

from chatbot.CivicBot import CivicBot
from face_detection.FaceDetectionNN import FaceDetectionNN

# Static class
class DataHolder:
    # Static variables
    convo = []
    first = "When it comes to politics, what's important to you? Feel free to speak candidly."
    bot = CivicBot()

    # Static methods
    @staticmethod
    def getSentence(sentence):
        return DataHolder.bot.getReply(sentence)


    @staticmethod
    def reset():
        DataHolder.convo = []
        DataHolder.bot.reset()


    @staticmethod
    def findFinal():
        cans = ["Amy Klobuchar.html", "Andrew Yang.html", "Bernie Sanders.html", "Cory Booker.html", "Deval Patrick.html", "Donald Trump.html", "Elizabeth Warren.html", "Joe Biden.html", "Joe Walsh.html", "Kamala Harris.html", "Marianna Williamson.html", "Mark Sanford.html", "Michael Bennet.html", "Michael Bloomberg.html", "Pete Buttigieg.html", "Tom Steyer.html", "Tulsi Gabbard.html"]
        return cans[DataHolder.bot.getFinal()]
