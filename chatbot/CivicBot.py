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
        self.DONE_STATE = 3
        self.FOLLOW_UP_QUESTIONS = ['Could you tell me a bit about your stance on abortions in America?', 'What is your opinion on empowering large corporations in America?', 'What do you think about the American prison system?', 'Tell about your opinions on the American education system.', 'Could you tell me about your opinions regarding the environment?', 'What do you think about the size of our government? Should the government be less involved in the lives of its citizens?', 'Tell me more about your stance on gun ownership in America.', 'What do you think of the American health care system?', 'How would you feel if the American government cut down on military spending?', 'Does the national debt in America worry you?', 'Are you proud to be an American right now?', 'Do you think America has secure borders?', 'What do you think would happen if the government lowered the amount of taxes everyone has to pay?']
        # Variables
        self.opinion = [0] * self.BOT_ONE.getSize() # STATE: 0 = NOT SPECIFIED, 1 = STRONG FOR, 2 = WEAK FOR, 3 = WEAK AGAINST, 4 = STRONG AGAINST
        self.done = 0; # STATE: 0 = JUST STARTED, 1 = ON THE SECOND QUESTION, 2 = ON THE THIRD QUESTION, 3 = DONE
        #self.done = 0; # STATE: 0 = JUST STARTED, 1 = ON THE SECOND QUESTION, 2 = DONE
        self.follow_ups = []
        self.currentOpinionState = 0;
        self.opinionTime = False;
        self.notEnoughInfo = False;
        self.knowledgeGain = 0;
        self.alreadyTried = False

    def reset(self):
        self.opinion = [0] * self.BOT_ONE.getSize()
        self.done = 0
        self.follow_ups = []

    def getReply(self, sentence):
        if self.opinionTime:
            self.opinion[self.currentOpinionState] = self.BOT_TWO.classify(sentence)[0][0] + 1
            print("New Opinion: ", self.opinion)
            self.knowledgeGain += 1
        else:
            classify = self.BOT_ONE.classify(sentence)
            print("Classifications Found: ", classify)
            if classify == []:
                return "Could you tell me a bit more information?"
            for tag in classify:
                self.follow_ups.append(tag)
            self.opinionTime = True
        while self.follow_ups != []:
            nextNum = self.follow_ups.pop()[0]
            print(nextNum)
            if self.opinion[nextNum] == 0:
                self.notEnoughInfo = False
                self.currentOpinionState = nextNum
                self.alreadyTried = False
                return self.FOLLOW_UP_QUESTIONS[nextNum]
        ## If we're here, then it is True that: self.follow_ups = []
        if self.notEnoughInfo and not self.alreadyTried:
            ## If we're here, then we didn't get any new information
            self.alreadyTried = True
            return "Could you tell me a bit more information? When it comes to politics, what else is important to you?"
        print("Next Step")
        self.opinionTime = False
        self.alreadyTried = False
        self.done += 1
        if (self.done >= self.DONE_STATE) or ((self.done + 1 >= self.DONE_STATE) and (self.knowledgeGain >= 4)):
            print("Conversation Over")
            return "NULL"
        print("Next Question")
        self.notEnoughInfo = True
        if self.done <= 1:
            return "When it comes to politics, what else is important to you? Once again, feel free to speak candidly."
        return "I'm getting some good information! Could you tell me about one or two more policies that are important to you?"
    def getFinal():
        return self.opinion
