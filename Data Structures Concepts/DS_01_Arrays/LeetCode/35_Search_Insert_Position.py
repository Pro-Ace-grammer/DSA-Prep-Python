'''
35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

'''


def searchInsertPosition(nums,target):
    if target in nums:
        return nums.index(target)
    elif target<nums[0]:
        return 0
    elif target>nums[-1]:
        return len(nums)
    
    for i in range(len(nums)-1):
        if nums[i]<target<nums[i+1]:
            return i+1
nums = [1,3,5,6]
target = 7
print(searchInsertPosition(nums,target))