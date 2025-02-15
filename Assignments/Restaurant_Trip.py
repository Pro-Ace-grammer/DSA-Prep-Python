
def solve(n, x, y):
    friends = list(zip(x, y))
    friends.sort(key=lambda f: f[1], reverse=True)
    # print(friends)
    visited = set()
    days = 0

    while len(visited) < n:
        group = []
        total_food = 0
        total_budget = 0

        for i in range(n):
            if i not in visited:
                group.append(i)
                total_food += friends[i][0]
                total_budget += friends[i][1]

        if len(group) >= 2 and total_budget >= total_food:
            visited.update(group)
            days += 1
            # print(visited)
        else:
            break
    
    return days

n=6
x = [8,3,9,2,4,5]
y = [5,3,1,4,5,10]
print(solve(n,x,y))