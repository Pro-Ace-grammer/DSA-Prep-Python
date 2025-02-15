'''
Maximum stones
Anish, Binish and Vivek are playing a game. They have n piles of stones where (n%3=0). In each turn you can select three piles from the total piles. Anish takes the maximum, then Vivek takes the second maximum and then Binish takes the third one.

Help Vivek get the maximum number of stones possible and return that number.

Input Format:

The first line contains an integer ( n ) (the number of piles).
The second line contains ( n ) integers representing the number of stones in each pile.
Output Format:

Return the maximum number of stones Vivek can get.
Sample Input:

6
2 4 9 8 11 2
Sample Output:

13
Explanation:

We can select the piles [11,9, 2] from which Anish will get 11 , Vivek will get 9 and Binish would get 2. The next piles that are left is [8, 4, 2] from which Anish will get 8, Vivek will get 4 and Binish would get 2. Thus the total number of stones that Vivek has is 9 + 4 = 13.

Constraints:

3<=n<=10^5
1<=a[i]<=10^4

'''

def MaximumPile(piles):
    piles.sort(reverse=True)
    triplets = []
    n = len(piles)
    for i in range(0, n, 2):
        if i + 2 < n:
            triplets.append([piles[i], piles[i+1], piles[-(i//3 + 1)]])
        if len(triplets)== n//3:
            break
    return sum([i[1] for i in triplets])

piles = [2, 4, 9, 8, 11, 2]
print(MaximumPile(piles))