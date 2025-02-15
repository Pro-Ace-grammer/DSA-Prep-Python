
def moveTwosToEnd(nums):
    n = len(nums)
    i = 0
    for j in range(n):
        if nums[j] != 2:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        print(nums)
    print(nums)

# Input Handling
nums = [1,2,2,3,4]
n = len(nums)

moveTwosToEnd(nums)
