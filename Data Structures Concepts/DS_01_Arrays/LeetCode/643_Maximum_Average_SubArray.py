'''
643. Maximum Average Subarray I
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000

'''


# def maxAverage(nums,k):
#     if len(nums)==k:
#         return sum(nums)/len(nums)
#     sub_arr = [nums[i:i+k] for i in range(len(nums)-k+1)]
#     max_avg = float('-inf')
#     for arr in sub_arr:
#         max_avg = max(max_avg,sum(arr)/len(arr))
#     return max_avg

def maxAverage(nums,k):
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    for i in range(k,len(nums)):
        curr_sum += nums[i]-nums[i-k] # here I am sliding the window
        max_sum = max(max_sum,curr_sum)
    return max_sum/k

nums = [5]
k = 1
print(maxAverage(nums,k))