def insertionSort(arr,n):
    for i in range(1,n):
        curr = arr[i]
        prev = i-1
        while prev>=0 and arr[prev]<curr:
            arr[prev+1]=arr[prev]
            prev-=1
        arr[prev+1]=curr

arr = [5,8,3,2,6,15,9,7,4,1]
n = len(arr)
insertionSort(arr,n)
print(arr)