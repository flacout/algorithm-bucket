#Uses python3

import sys
from operator import itemgetter


global order
order =1

def acyclic(adj):
    visited = { k:False for k in range(len(adj))}
    postorder = [0 for _ in range(len(adj))]
    for k in visited.keys():
        if not visited[k]:
            explore(k, adj, visited, postorder)

    indices, L_sorted = zip(*sorted(enumerate(postorder), key=itemgetter(1), reverse=True))
    return indices

def explore(v, adj, visited, postorder):
    global order
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            explore(w, adj, visited, postorder)
    postorder[v]=order
    order+=1


'''
def dfs(adj, used, order, x):
    #write your code here
    pass

def toposort(adj):
    used = [0] * len(adj)
    order = []
    #write your code here
    return order
'''

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    #order = toposort(adj)
    order = acyclic(adj)
    for x in order:
        print(x + 1, end=' ')

