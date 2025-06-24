'''
You are given a string s. Reorder the string using the following algorithm:

Remove the smallest character from s and append it to the result.
Remove the smallest character from s that is greater than the last appended character, and append it to the result.
Repeat step 2 until no more characters can be removed.
Remove the largest character from s and append it to the result.
Remove the largest character from s that is smaller than the last appended character, and append it to the result.
Repeat step 5 until no more characters can be removed.
Repeat steps 1 through 6 until all characters from s have been removed.
If the smallest or largest character appears more than once, you may choose any occurrence to append to the result.

Return the resulting string after reordering s using this algorithm.
'''

def sortString(s: str) -> str:
    counter = [0]*26
    for ch in s:
        counter[ord(ch)-ord('a')]+=1
    ans = []
    while len(ans)<len(s):
        for i in range(26):
            if counter[i]:
                ans.append(chr(i+ord('a')))
                counter[i]-=1
        for i in range(25,-1,-1):
            if counter[i]:
                ans.append(chr(i+ord('a')))
                counter[i]-=1
    return ''.join(ans)
    