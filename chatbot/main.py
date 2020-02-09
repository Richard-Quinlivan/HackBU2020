## Nick Pellegrino
## CivicBot main.py
## Run this file directly to test out CivicBot

from CivicBot import CivicBot

def main():
    bot = CivicBot()
    outputSentence = ""

    # First question
    print("\nWhen it comes to politics, what's important to you? Feel free to speak candidly.")
    inputSentence = input("\nEnter input: ")

    # The rest of the conversation
    while outputSentence != "NULL":
        outputSentence = bot.getReply(inputSentence)
        print("\n" + outputSentence)
        if outputSentence != "NULL":
            inputSentence = input("\nEnter input: ")

    print("Final Opinion: ", bot.opinion)

if __name__ == '__main__':
    main()
