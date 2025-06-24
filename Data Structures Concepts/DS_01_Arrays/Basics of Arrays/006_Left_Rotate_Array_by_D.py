'''
Left rotate an array by D places
'''

def rotateByDPlaces(arr,d):
    n = len(arr)
    d = d%n
    temp = list()
    for i in range(d):
        temp.append(arr[i])
    for i in range(d,n):
        arr[i-d]=arr[i]
    for i in range(n-d,n):
        arr[i] = temp[i-(n-d)]
    return arr

arr = [1,2,3,4,5]
d = 3
print(rotateByDPlaces(arr,d))