'''
Find the median of two sorted arrays
'''

# def union(a,b,n,m):
#     i,j = 0,0
#     unionArr = []
#     while (i<n) and (j<m):
#         if a[i]<b[j]:
#             if len(unionArr)==0 or unionArr[-1]!=a[i]:
#                 unionArr.append(a[i])
#             i+=1
#         else:
#             if len(unionArr)==0 or unionArr[-1]!=b[j]:
#                 unionArr.append(b[j])
#             j+=1
#     while i<n:
#         if len(unionArr)==0 or unionArr[-1]!=a[i]:
#             unionArr.append(a[i])
#         i+=1
#     while j<m:
#         if len(unionArr)==0 or unionArr[-1]!=b[j]:
#             unionArr.append(b[j])
#         j+=1
#     return unionArr

# def getMedian(ar1,ar2,n,m):
#     unionArr = union(ar1,ar2,n,m)
#     print(unionArr)
#     if len(unionArr)%2==0:
#         mid = (len(unionArr)//2)-1
#         median=(unionArr[mid]+unionArr[mid+1])//2
#     else:
#         mid = len(unionArr)//2
#         median=unionArr[mid]
#     return median




class Solution:
    def union(self,a,b,n,m):
      i,j = 0,0
      unionArr = []
      while (i<n) and (j<m):
          if a[i]<b[j]:
              if len(unionArr)==0 or unionArr[-1]!=a[i]:
                  unionArr.append(a[i])
              i+=1
          else:
              if len(unionArr)==0 or unionArr[-1]!=b[j]:
                  unionArr.append(b[j])
              j+=1
      while i<n:
          if len(unionArr)==0 or unionArr[-1]!=a[i]:
              unionArr.append(a[i])
          i+=1
      while j<m:
          if len(unionArr)==0 or unionArr[-1]!=b[j]:
              unionArr.append(b[j])
          j+=1
      return unionArr

    def getMedian(self,ar1,ar2,n,m):
        unionArr = self.union(ar1,ar2,n,m)
        print(unionArr)
        if len(unionArr)%2==0:
            mid = (len(unionArr)//2)-1
            median=(unionArr[mid]+unionArr[mid+1])//2
        else:
            mid = len(unionArr)//2
            median=unionArr[mid]
        return median


ar1 = [2,1,9]
ar2 = [2,5,11]
n = len(ar1)
m = len(ar2)
s = Solution()
print(s.getMedian(ar1,ar2,n,m))
