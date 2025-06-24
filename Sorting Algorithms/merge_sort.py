def merge(arr,start,mid,end):
    i,j=start,mid+1
    temp = []
    while i<=mid and j<=end:
        if arr[i]>arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    while i<=mid:
        temp.append(arr[i])
        i+=1
    while j<=end:
        temp.append(arr[j])
        j+=1

    for i in range(0,len(temp)):
        arr[i+start] = temp[i]

def mergeSort(arr,start,end):
    if start<end:
        mid = start + (end-start)//2
        mergeSort(arr,start,mid)
        mergeSort(arr,mid+1,end)
        merge(arr,start,mid,end)

arr = [5,8,3,2,6,15,9,7,4,1]
start,end = 0,len(arr)-1
mergeSort(arr,start,end)
print(arr)