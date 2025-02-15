'''

'''

def countNegatives(grid):
    count = 0
    for nums in grid:
        for n in nums:
            if n<0:
                count+=1
    return count

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))