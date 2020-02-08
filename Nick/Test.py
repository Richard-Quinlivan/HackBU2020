## Nick Pellegrino
## ChatBot Tester (uses ChatBot.py)
## Run this file directly to test the ChatBot in terminal

from ChatBot import ChatBot

def main():
    bot = ChatBot()
    print('\n\n')
    while(True):
        inputSentence = input('Enter input: ')
        bot.printResults(inputSentence)

if __name__ == '__main__':
    main()
