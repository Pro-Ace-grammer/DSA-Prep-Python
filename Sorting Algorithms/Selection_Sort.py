'''
Selection Sort
Selection Sort is a simple sorting algorithm that works by repeatedly finding theminimum element from the unsorted portion of the list and swapping it with the element at the beginning of the sorted portion. This process continues until the entire list is sorted.

'''

def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        minJ = i
        for j in range(i+1,n):
            if arr[j]<arr[minJ]:
                minJ = j
        arr[i],arr[minJ] = arr[minJ],arr[i]
    return arr

arr = [2,5,9,4,1,8,10]
print(selectionSort(arr))