import random

#candidates = array of arrays for each candidates' views
#user = array of user's views
#returns index of closest candidate
def findClosest(candidates, user):
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
