def subsequence(ind:int, arr:list, sub: list):
    if ind>=len(arr):
        print(sub)
        return
    sub.append(arr[ind])
    subsequence(ind+1,arr,sub)
    sub.pop()
    subsequence(ind+1,arr,sub)


# def subsequence(arr:list):
#     n = len(arr)
#     for num in range(0, 2**n):
#         sub = []
#         for i in range(0,n):
#             if num & (1<<i):
#                 sub += [arr[i]]
#         print(sub)
    
arr = [1,2,3]
subsequence(0,arr,[])
