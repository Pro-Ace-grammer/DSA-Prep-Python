'''

'''
# def countPoints(rings: str) -> int:
#     rods = {i:'' for i in range(10)}
#     for i in range(1,len(rings),2):
#         if rings[i-1] not in rods[int(rings[i])]:
#             rods[int(rings[i])] = ''.join(sorted(rods[int(rings[i])]+rings[i-1]))
#         print(rods)
#         # if 'BGR' in rods[int(rings[i])]:
#             # return int(rings[i])+1
#     return 0


# Questions is to find how many rods ??
def countPoints(rings: str) -> int:
    rods = {i:set() for i in range(10)}
    for i in range(1, len(rings), 2):
        rod_position = int(rings[i])
        rods[rod_position].add(rings[i - 1])
        
    return sum(len(colors) == 3 for colors in rods.values())

rings = "G3R3R7B7R5B1G8G4B3G6"
print(countPoints(rings))