# mat = [[1,0,0,0],
#  [1,1,1,1],
#  [1,0,0,0],
#  [1,0,0,0]]

# count = {i:mat[i].count(1) for i in range(len(mat))}
# print(count)
# print(sorted(count, key=lambda x: count[x]))




# def subSets(arr):
#     result = []
#     def combo(curr_combo,start):
#         if curr_combo:
#             result.append(curr_combo[:])
#         for i in range(start,len(arr)):
#             curr_combo.append(arr[i])
#             combo(curr_combo,i+1)
#             curr_combo.pop()
#     combo([],0)
#     return result

# print(subSets([1,2,3]))
# n = [1,2,3,4,2].index(2,2)
# print(n)


# def findErrorNums(nums):
#     dup_val = 0
#     for i in nums:
#         if nums.count(i)>1:
#             return [i,nums[nums.index(i,i)]+1]

# print(findErrorNums([1,1]))



# def dutchFlagSort(nums):
#     low,mid,high = 0,0,len(nums)-1
#     while mid<=high:
#         if nums[mid] == 2:
#             nums[mid],nums[high]=nums[high],nums[mid]
#             high-=1
#         elif nums[mid]==0:
#             nums[low],nums[mid]=nums[mid],nums[low]
#             low+=1
#             mid+=1
#         else:
#             mid+=1
#         # print(nums)
#         # print(low,mid,high)
#     print(nums)

# nums = [2,0,2,1,1,0]
# dutchFlagSort(nums)






# def solve(inventory1, inventory2):
#     n1,n2,i,j = len(inventory1),len(inventory2),0,0
#     res = []
#     while i<n1 and j<n2:
#         if inventory1[i]<inventory2[j]:
#             res.append(inventory1[i])
#             i+=1
#         else:
#             res.append(inventory2[j])
#             j+=1
#     while i<n1:
#         res.append(inventory1[i])
#         i+=1
#     while j<n2:
#         res.append(inventory2[j])
#         j+=1
#     return res

# a=['book', 'enchanted', 'spell', 'wand']
# b=['ancient', 'dragon', 'magic', 'scroll']
# print(*solve(a,b))