## Brendan Klayman & Nick Pellegrino
## Opinion Similarity Calculator
## Run this file to test the calculator

import random

# candidates = array of arrays for each candidates' views
# user = array of user's views
# returns index of closest candidate
class CandCalc:
    def findClosest(self, candidates, user):
        candidatesDistances = []
        for i in range(0, len(candidates)):
            difference = 0
            for j in range(0, len(candidates[i])):
                if(user[j] != 0):
                    difference += abs(candidates[i][j] - user[j])
            print(candidates[i], " ", difference)
            candidatesDistances.append(difference)
        min = 9999
        index = 0
        for i in range(len(candidatesDistances)):
            if candidatesDistances[i] < min:
                min = candidatesDistances[i]
                index = i
        bestCandidates = [i for i in range(len(candidatesDistances)) if candidatesDistances[i] <= min]
        return random.choice(bestCandidates)

def main():
    print(CandCalc().findClosest([[2,3,4,3,3,2,4,3,1,4,3,3,4], [1,3,4,2,4,1,3,3,1,4,3,3,4], [1,4,4,4,4,1,3,4,1,4,4,1,4], [1,3,4,3,3,1,4,4,4,4,3,1,4], [2,3,3,3,3,2,4,3,2,3,3,2,3], [4,1,1,1,1,4,1,1,4,1,1,4,2], [1,4,4,4,4,1,4,4,1,4,4,1,1], [2,3,4,3,1,2,3,3,4,3,3,3,3], [4,2,2,2,3,3,2,1,3,2,2,4,2], [1,3,4,2,2,1,4,3,1,4,4,1,4], [2,3,4,4,3,1,4,3,2,4,4,1,4], [4,2,2,2,4,4,2,1,3,1,2,4,2], [1,4,4,2,2,1,4,2,4,4,4,2,4], [2,3,3,2,3,2,4,3,2,3,3,2,4], [1,4,4,2,3,2,3,3,1,4,3,2,3], [3,3,4,3,4,1,3,3,2,4,3,1,4], [1,3,4,4,3,2,4,3,1,3,4,3]], [3, 0, 0, 0, 4, 0, 2, 0, 0, 0, 0, 0, 0]))
    print(CandCalc().findClosest([[2,3,4,3,3,2,4,3,1,4,3,3,4], [1,3,4,2,4,1,3,3,1,4,3,3,4], [1,4,4,4,4,1,3,4,1,4,4,1,4], [1,3,4,3,3,1,4,4,4,4,3,1,4], [2,3,3,3,3,2,4,3,2,3,3,2,3], [4,1,1,1,1,4,1,1,4,1,1,4,2], [1,4,4,4,4,1,4,4,1,4,4,1,1], [2,3,4,3,1,2,3,3,4,3,3,3,3], [4,2,2,2,3,3,2,1,3,2,2,4,2], [1,3,4,2,2,1,4,3,1,4,4,1,4], [2,3,4,4,3,1,4,3,2,4,4,1,4], [4,2,2,2,4,4,2,1,3,1,2,4,2], [1,4,4,2,2,1,4,2,4,4,4,2,4], [2,3,3,2,3,2,4,3,2,3,3,2,4], [1,4,4,2,3,2,3,3,1,4,3,2,3], [3,3,4,3,4,1,3,3,2,4,3,1,4], [1,3,4,4,3,2,4,3,1,3,4,3]], [1,0,4,2,0,0,3,0,0,0,0,0,0])) ## Correct answer: 2
    print(CandCalc().findClosest([[2,3,4,3,3,2,4,3,1,4,3,3,4], [1,3,4,2,4,1,3,3,1,4,3,3,4], [1,4,4,4,4,1,3,4,1,4,4,1,4], [1,3,4,3,3,1,4,4,4,4,3,1,4], [2,3,3,3,3,2,4,3,2,3,3,2,3], [4,1,1,1,1,4,1,1,4,1,1,4,2], [1,4,4,4,4,1,4,4,1,4,4,1,1], [2,3,4,3,1,2,3,3,4,3,3,3,3], [4,2,2,2,3,3,2,1,3,2,2,4,2], [1,3,4,2,2,1,4,3,1,4,4,1,4], [2,3,4,4,3,1,4,3,2,4,4,1,4], [4,2,2,2,4,4,2,1,3,1,2,4,2], [1,4,4,2,2,1,4,2,4,4,4,2,4], [2,3,3,2,3,2,4,3,2,3,3,2,4], [1,4,4,2,3,2,3,3,1,4,3,2,3], [3,3,4,3,4,1,3,3,2,4,3,1,4], [1,3,4,4,3,2,4,3,1,3,4,3]], [4,1,1,1,1,4,1,1,4,1,1,4,2])) ## Correct answer: 5

if __name__ == '__main__':
    main()
