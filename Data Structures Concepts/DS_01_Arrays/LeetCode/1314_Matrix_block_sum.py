'''
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.
 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]


Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 
'''

def matSum(mat,k):
    row = len(mat)
    col = len(mat[0])
    out =  []
    for i in range(row):
        out.append([])
        for j in range(col):
            sum_ = 0
            for r in range(i-k,i+k+1):
                for c in range(j-k,j+k+1):
                    if r < row and r>=0 and c < col and c>=0:
                        sum_ += mat[r][c]
            out[-1].append(sum_)
    return out






def matrixSum(mat,k):
    m,n = len(mat), len(mat[0])
    prefix = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            prefix[i+1][j+1] = mat[i][j] + prefix[i+1][j] + prefix[i][j+1] - prefix[i][j]
    result = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            r1,c1 = max(0,i-k),max(0,j-k)
            r2,c2 = min(m-1,i+k),min(n-1,j+k)

            result[i][j] = prefix[r2+1][c2+1]-prefix[r1][c2+1]-prefix[r2+1][c1]+prefix[r1][c1]
    return result

mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(matrixSum(mat,k))