#Uses python3

import sys

sys.setrecursionlimit(200000)

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



def second(adj, indices):
    visited2 = { k:False for k in range(len(adj))}
    # label is the number of Strongly connected component
    label = 0
    for v in indices:
        if not visited2[v]:
            explore2(v, adj, visited2)
            label+=1
    return label

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
    adjR = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adjR[b - 1].append(a - 1)
    indices = acyclic(adjR)
    #print(indices)
    print(second(adj, indices))

'''
def number_of_strongly_connected_components(adj):
    result = 0
    #write your code here
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
'''
