'''
'''

# from typing import List
# class Solution:
#     def kthDistinct(self, arr: List[str], k: int) -> str:
#         disticts = {i:arr.count(i) for i in arr}
#         for key, val in disticts.items():
#             if val==1:
#                 k-=1
#             if k==0:
#                 return key
#         return ""

s = 'xyzzaz'
count=0
for i in range(len(s)-2):
    subst = s[i:i+3]
    print(su)
    if len(subst)==set(subst):
        count+=1
print(count)