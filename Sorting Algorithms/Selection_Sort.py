def selectionSort(arr,n):
    for i in range(n-1):
        minIndex = i
        for j in range(i+1,n):
            if arr[j]<arr[minIndex]:
                minIndex = j
        arr[i],arr[minIndex] = arr[minIndex],arr[i]

arr = [5,8,3,2,6,15,9,7,4,1]
n = len(arr)
selectionSort(arr,n)
print(arr)