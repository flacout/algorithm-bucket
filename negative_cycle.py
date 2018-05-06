#Uses python3
# TODO handle not connected case

import sys
from queue import Queue

def negative_cycle(adj, cost):
    dist = [float('inf') for _ in range(len(adj))]
    discover = [False for _ in range(len(adj))]

    # find distances from node 0. 
    s = 0
    dist[s] = 0
    q = Queue()
    relaxed = False

    while True:
        # 3 iteration is usualy enough to stabilize the distances
        for _ in range(3):
            visited = [False for _ in range(len(adj))]
            relaxed = False
            q.put(s)
            visited[s] = True
            discover[s] = True
            # BFS to relax all edges on one connected component
            while (not q.empty()):
                u = q.get()
                for w_index, v in enumerate(adj[u]):
                    if dist[v] > (dist[u] + cost[u][w_index]):
                        dist[v] = (dist[u] + cost[u][w_index])
                        relaxed = True
                    if visited[v]==False: 
                        q.put(v)
                        visited[v]=True
                        discover[v] = True

        if relaxed == True: return 1
        elif False in discover:
            # get next starting point for new connected component
            s = discover.index(False)
            dist[s] = 0
            continue
        else: return 0


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
    print(negative_cycle(adj, cost))
