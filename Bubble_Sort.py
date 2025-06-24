'''
Bubble Sort is a basic sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the entire list is sorted.
'''

# def bubbleSort(arr,n):
#     for i in range(n):
#         swapped = False # taking one flag to check if the swapping is done or not
#         for j in range(n-i-1): # For each pass the last element will be sorted. so thats y we take n-i-1
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#                 swapped=True
#         if not swapped:
#             return arr

# arr = [5,1,3,6,13,7,2,9,4,12]
# n = len(arr)
# print(bubbleSort(arr,n))




############################# QUESTION ON BUBBLE SORT ###############################


'''
Bubble Sort
Anish and Binish are playing a game. They both have to pick 'n' stones of varying sizes with non-duplicates and give their set of stones to the other.
They have to sort these stones in increasing order but are allowed to do just one operation on them: they can swap any adjacent stones with each other. The one who sorts their set of stones with the least number of swaps wins. You are given two arrays named 'Anish' and 'Binish' representing the size of stones that they have to sort. Determine the winner of the game.

Note: If the game is a tie, print out "Tie".

Input Format:

The first line contains an integer ( n ) (1 ≤ ( n ) ≤ 1000), the number of stones.
The second line contains ( n ) integers representing the sizes of stones Anish has.
The third line contains ( n ) integers representing the sizes of stones Binish has.
Output Format:

Print "Anish" if Anish wins.
Print "Binish" if Binish wins.
Print "Tie" if the game is a tie.
Sample Input 1:

5
7 2 8 9 5
4 6 2 5 3
Sample Output 1:

Anish
Explanation:

Anish can sort his stones with fewer swaps compared to Binish.

Constraints:

1<=n<=1000

1<=s[i]<=10^5
'''
def game(a, b, n):
    anish_swaps=0
    binish_swaps=0
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                anish_swaps+=1
                print(a)
            if b[j]>b[j+1]:
                b[j],b[j+1]=b[j+1],b[j]
                binish_swaps+=1
    print(anish_swaps)
    print(binish_swaps)
    if anish_swaps==binish_swaps:
        return 'Tie'
    return "Anish" if anish_swaps>binish_swaps else 'Binish'

a = [7,2,8,9,5]
b = [4,6,2,5,3]
n = 5
print(game(a,b,n))