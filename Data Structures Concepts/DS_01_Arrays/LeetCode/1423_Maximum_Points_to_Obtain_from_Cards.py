'''

'''

from itertools import combinations
def maxScore(cardPoints,k):
    sub_arr = cardPoints[:k]+cardPoints[len(cardPoints)-k:]
    
    

cardPoints = [100,40,17,9,73,75]
k = 3
print(maxScore(cardPoints,k))

