'''

'''

def kWeakestRows(mat,k):
    counts = {i:mat[i].count(1) for i in range(len(mat))}
    return sorted(counts,key=lambda i:counts[i])[:k]

mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
k = 2
print(kWeakestRows(mat,k))