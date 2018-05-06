#Uses python3

import sys

def reach(adj, x, y):
    #write your code here
    return 0
def explore(v, V, visited):
    visited[v]=True
    for w in V[v]:
        if w not in visited:
            explore(w, V, visited)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]

    # make V a dict of adjacent list
    V = {k:[] for k in range(1,n+1)}
    #adj = [[] for _ in range(n)]
    #x, y = x - 1, y - 1
    for (a, b) in edges:
        V[a].append(b)
        V[b].append(a)
    #    adj[a - 1].append(b - 1)
    #    adj[b - 1].append(a - 1)
    #print(reach(adj, x, y))

    visited={}
    explore(x, V, visited)
    if y in visited: print(1)
    else: print(0)
