'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array. 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

'''


# def smallerCount(nums):
#     out = []
#     for i in range(len(nums)):
#         count = 0
#         for j in range(len(nums)):
#             if i!=j and nums[i]>nums[j]:
#                 count += 1
#         out.append(count)

#     return out


def smallerCount(nums):
    sorted_nums = sorted(nums)
    num_map = {}
    for ind,value in enumerate(sorted_nums):
        if value not in num_map:
            num_map[value] = ind 
            
    return [num_map[num] for num in nums]

nums = [8,1,2,2,3]
print(smallerCount(nums))