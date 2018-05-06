#uses python3

import sys
import threading
from queue import Queue

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, vertex, parent):
    for child in tree[vertex].children:
        if child != parent:
            dfs(tree, child, vertex)

    # This is a template function for processing a tree using depth-first search.
    # Write your code here.
    # You may need to add more parameters to this function for child processing.



def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    dfs(tree, 0, -1)
    # You must decide what to return.
    return 0

def BFS(adj, s, tree2):
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
                tree2[u].append(v)
    return

def funParty(v, tree, D, weight):
    if D[v] == float('inf'):
        if len(tree[v])==0:
            D[v] = weight[v]
        else:
            # grandchildren
            m1 = weight[v]
            for u in tree[v]:
                for uu in tree[u]:
                    m1 = m1 + funParty(uu, tree, D, weight)
            # children
            m0 = 0
            for u in tree[v]:
                m0 = m0 + funParty(u, tree, D, weight)
            D[v] = max(m1, m0)
    return D[v]

def main():
    #tree = ReadTree();
    #weight = MaxWeightIndependentTreeSubset(tree);
    #print(weight)
    size = int(input())
    weight = [ w for w in map(int, input().split())]
    #print(weight)
    tree = [ [] for _ in range(size)]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)
        #if a<b :
        #    tree[a-1].append(b-1)
        #else:
        #    tree[b-1].append(a-1)
    #print(tree)
    D=[float('inf')]*len(tree)
    tree2 = [ [] for _ in range(size)]
    BFS(tree, 0, tree2)
    #print(tree2)
    solution = funParty(0, tree2, D, weight)
    print(solution)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
