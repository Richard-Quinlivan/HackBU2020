## Nick Pellegrino
## CivicBot (uses ChatBot 1 & 2)
## No need to run this file directly

from chatbot1.ChatBot import ChatBot1
from chatbot2.ChatBot import ChatBot2

class CivicBot:
    def __init__(self):
        # Constants
        self.BOT_ONE = ChatBot1()
        self.BOT_TWO = ChatBot2()
        self.FOLLOW_UP_QUESTIONS = ['Could you tell me a bit about your stance on abortions in America?', 'What is your opinion on empowering large corporations in America?', 'What do you think about the American prison system?', 'Tell about your opinions on the American education system.', 'Could you elaborate on your opinions regarding the environment?', 'What do you think about the size of our government? Should the government be less involved in the lives of its citizens?', 'Tell me more about your stance on gun ownership in America', 'What do you think of the American health care system?', 'How would you feel if the American government cut down on military spending?', 'Does the national debt in America worry you?', 'Are you proud to be an American right now?', 'Do you think America has secure borders?', 'What do you think would happen if the government lowered the amount of taxes everyone has to pay?']
        # Variables
        self.opinion = [0] * self.BOT_ONE.getSize() # STATE: 0 = NOT SPECIFIED, 1 = FOR, 2 = AGAINST
        self.done = 0; # STATE: 0 = JUST STARTED, 1 = ON THE FIRST QUESTION, 2 = ON THE SECOND QUESTION, 3 = DONE
        self.follow_ups = []

    def reset(self):
        self.opinion = [0] * self.BOT_ONE.getSize()
        self.done = 0
        self.follow_ups = []

    def getReply(self, sentence):
        if self.follow_ups == []:
            self.opinion += 1
            if self.opinion >= 3:
                return "NULL"
            if self.opinion <= 1:
                return "When it comes to politics, what's important to you? Feel free to speak candidly."
            return "Could you tell me about a couple more policies that matter a lot to you?"
        else:
            nextNum = self.follow_ups.pop()
