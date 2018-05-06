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

    indices, L_sorted = zip(*sorted(enumerate(postorder), key=itemgetter(1)))
    return indices

def explore(v, adj, visited, postorder):
    global order
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            explore(w, adj, visited, postorder)
    postorder[v]=order
    order+=1



def second(adj, indices):
    visited2 = { k:False for k in range(len(adj))}
    # label is the number of Strongly connected component
    label = 0
    for v in indices:
        if not visited2[v]:
            explore2(v, adj, visited2)
            label+=1
    #print(label)
    if label==len(adj): return 0
    else: return 1

def explore2(v, adj, visited2):
    visited2[v] = True
    for w in adj[v]:
        if not visited2[w]:
            explore2(w, adj, visited2)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # adjacent list of vertex
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    indices = acyclic(adj)
    #print(indices)
    print(second(adj, indices))
