'''
To check if the given sentence is pangram or not
'''

def checkIfPangram(sentence: str) -> bool:
    for i in range(ord('a'),ord('z')+1):
        if chr(i) not in sentence:
            return False
    return True

