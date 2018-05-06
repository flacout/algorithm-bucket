# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

# find with path compression
def getParent(i, parent):
    # find parent and compress path
    if parent[i] != i:
        parent[i] = getParent(parent[i], parent)
    return parent[i]

# union by rank
def merge(destination, source, parent, rank, ans):
    realDestination, realSource = getParent(destination, parent), getParent(source, parent)
    if realDestination == realSource:
        return ans
    if rank[realDestination] > rank[realSource]: 
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        nbRows = lines[realDestination]
    else :
        parent[realDestination] = realSource
        lines[realSource] += lines[realDestination]
        nbRows = lines[realSource]
        if rank[realDestination] == rank[realSource]:
            rank[realSource] +=1
    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    if nbRows > ans : ans = nbRows
    return ans

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    ans = merge(destination - 1, source - 1, parent, rank, ans)
    print(ans)
    
