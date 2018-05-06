#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    dist = [float('inf') for _ in range(len(adj))]
    # keep prev if you want to reconstruct the path
    #prev = [None for _ in range(len(adj))]
    dist[s] = 0
    pQueue = [float('inf') for _ in range(len(adj))]
    pQueue[s] = 0
    correctSpace = {}

    minimum = 0
    u = s
    while (minimum !=float('inf')):
        # u is a node with correct distance to s now so place it in correct Space
        correctSpace[u] = True

        # relax all adjacent nodes from u
        for w_index, v in enumerate(adj[u]):
            if (v not in correctSpace) and (dist[v] > (dist[u] + cost[u][w_index])):
                dist[v] = (dist[u] + cost[u][w_index])
                #prev[v]=u
                pQueue[v] = dist[v]

        # remove u from priority queue and find next minimum node in pQueue
        pQueue[u] = float('inf')
        minimum = min(pQueue)
        u = pQueue.index(minimum)

    #print("distances", dist)
    #print("priority queue", pQueue)
    if dist[t] == float('inf'): return -1
    else: return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
