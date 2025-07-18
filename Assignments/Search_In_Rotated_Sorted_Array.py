'''
Search in rotated sorted array...
'''
# [7,8,9,1,2,3,4,5]
def search(arr,target):
    low,high=0,len(arr)-1
    while low<=high:
        mid = low + (high-low)//2
        if arr[mid]==target:
            return mid
        if arr[low]<=arr[mid] and arr[low]<=target<=arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1

arr = [7,8,9,1,2,3,4,5]
target = 1
print(search(arr,target))