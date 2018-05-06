#Uses python3

import sys
from queue import Queue

'''
create a shortest path tree from node 0
if inside a layer there is connection between nodes the graph is NOT bipartite
if there is no edge connecting 2 nodes in the same layer it is bipartite
   A
  / \    Bipartite
  B C


   A
  / \    Not Bipartite
  B-C
'''

def bipartite(adj):
    dist = [-1 for _ in range(len(adj))]
    prev = [None for _ in range(len(adj))]
    dist[0] = 0
    q = Queue()
    q.put(0)

    while (not q.empty()):
        u = q.get()
        for v in adj[u]:
            if dist[v] == dist[u] : return 0
            if dist[v] == -1 :
                q.put(v)
                dist[v] = dist[u] + 1
                prev[v]=u
    return 1

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
    print(bipartite(adj))
