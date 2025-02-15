'''
Remove duplicates in-place from sorted Array
'''
# 2-Pointer Approach

def removeDuplicates(arr,n):
    i = 0
    for j in range(1,n):
        if arr[j]!=arr[i]:
            arr[i+1]=arr[j]
            i+=1
    return i+1

arr = [1,1,2,2,2,3,3]
n = len(arr)
print(removeDuplicates(arr,n))