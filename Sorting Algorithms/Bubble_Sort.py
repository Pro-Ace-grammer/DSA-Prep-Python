def bubbleSort(arr : list[int],n):
    for i in range(0,n):
        isSwapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                isSwapped = True
        if not isSwapped:
            break

arr = [5,8,3,2,9,7,4,1]
n = len(arr)
bubbleSort(arr,n)
print(arr)