## Nick Pellegrino
## DataHolder holds data in a static way
## No need to run this file directly

class DataHolder:
    convo = []
    first = "When it comes to politics, what's important to you? Feel free to speak candidly."
    replyTo = "reply to "

    @staticmethod
    def getSentence(sentence):
        return DataHolder.replyTo + sentence
