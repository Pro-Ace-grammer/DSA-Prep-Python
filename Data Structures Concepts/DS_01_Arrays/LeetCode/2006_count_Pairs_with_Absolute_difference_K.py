'''
2006. Count Number of Pairs With Absolute Difference K

Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
 

Example 1:

Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
Example 2:

Input: nums = [1,3], k = 3
Output: 0
Explanation: There are no pairs with an absolute difference of 3.
Example 3:

Input: nums = [3,2,1,5,4], k = 2
Output: 3
Explanation: The pairs with an absolute difference of 2 are:
- [3,2,1,5,4]
- [3,2,1,5,4]
- [3,2,1,5,4]

'''

def countKDifference(nums,k):
    # count = 0
    # for i in range(len(nums)-1):
    #     for j in range(i+1,len(nums)):
    #         if abs(nums[i]-nums[j]) == k:
    #             count += 1

    # return count
    seen = {}
    counter =0
    for  num in nums:
        temp,temp2 = num-k,num+k
        if temp in seen:
            counter+=seen[temp]
        if temp2 in seen:
            counter+=seen[temp2]

        seen[num] += 1
    return counter

nums = [3,2,1,5,4]
k = 2
print(countKDifference(nums,k))