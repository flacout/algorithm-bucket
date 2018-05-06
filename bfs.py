#Uses python3

import sys
from queue import Queue

def distance(adj, s, t):
    #print("adj", adj)
    tree = BFS(adj, s)
    #print("tree", tree)
    if tree[t] == None : return -1
    path = reconstructPath(s, t, tree)
    #print("path", path)
    return len(path)


def BFS(adj, s):
    dist = [-1 for _ in range(len(adj))]
    prev = [None for _ in range(len(adj))]
    dist[s] = 0
    q = Queue()
    q.put(s)

    while (not q.empty()):
        u = q.get()
        for v in adj[u]:
            if dist[v] == -1 :
                q.put(v)
                dist[v] = dist[u] + 1
                prev[v]=u
    return prev

def reconstructPath(s, u, tree):
    path = []
    while u!=s:
        path.append(u)
        u = tree[u]
    return path



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
