'''
Find the union of two sorted arrays...
'''

def union(a,b):
    n1,n2 = len(a),len(b)
    i,j = 0,0
    unionArr = []
    while (i<n1) and (j<n2):
        if a[i]<b[j]:
            if len(unionArr)==0 or unionArr[-1]!=a[i]:
                unionArr.append(a[i])
            i+=1
        else:
            if len(unionArr)==0 or unionArr[-1]!=b[j]:
                unionArr.append(b[j])
            j+=1
    while i<n1:
        if len(unionArr)==0 or unionArr[-1]!=a[i]:
            unionArr.append(a[i])
        i+=1
    while j<n2:
        if len(unionArr)==0 or unionArr[-1]!=b[j]:
            unionArr.append(b[j])
        j+=1
    return unionArr

a = [1,2,2,3,3,4,5]
b = [2,2,3,3,4,5,6,7]
print(union(a,b))