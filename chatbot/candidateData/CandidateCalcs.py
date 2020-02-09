import random

#candidates = array of arrays for each candidates' views
#user = array of user's views
#returns index of closest candidate

class CandCalc:
    def findClosest(self, candidates, user):
        largestDifference = 42
        closestCandidates = []
        for i in range(0, len(candidates)):
            difference = 0
            for j in range(0, len(candidates[i])):
                if(candidates[i][j] != 0):
                    difference += abs(candidates[i][j] - user[j])
            if(difference == largestDifference):
                closestCandidates.append(i)
            else:
                closestCandidates = [i]
        if(len(closestCandidates) > 1):
            winner = random.randInt(0, len(closestCandidates))
            closestCandidates = [closestCandidates[winner]]
        return closestCandidates[0]

def main():
    print(CandCalc().findClosest([[2,3,4,3,3,2,4,3,1,4,3,3,4], [1,3,4,2,4,1,3,3,1,4,3,3,4], [1,4,4,4,4,1,3,4,1,4,4,1,4], [1,3,4,3,3,1,4,4,4,4,3,1,4], [2,3,3,3,3,2,4,3,2,3,3,2,3], [4,1,1,1,1,4,1,1,4,1,1,4,2], [1,4,4,4,4,1,4,4,1,4,4,1,1], [2,3,4,3,1,2,3,3,4,3,3,3,3], [4,2,2,2,3,3,2,1,3,2,2,4,2], [1,3,4,2,2,1,4,3,1,4,4,1,4], [2,3,4,4,3,1,4,3,2,4,4,1,4], [4,2,2,2,4,4,2,1,3,1,2,4,2], [1,4,4,2,2,1,4,2,4,4,4,2,4], [2,3,3,2,3,2,4,3,2,3,3,2,4], [1,4,4,2,3,2,3,3,1,4,3,2,3], [3,3,4,3,4,1,3,3,2,4,3,1,4], [1,3,4,4,3,2,4,3,1,3,4,3]], [3, 0, 0, 0, 4, 0, 2, 0, 0, 0, 0, 0, 0]))

if __name__ == '__main__':
    main()
