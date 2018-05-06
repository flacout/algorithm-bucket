# python3
import sys, threading
from operator import itemgetter

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**28)  # new thread will get stack of such size


# for finding SCC.
global order
order =1

# read input
V, C = map(int, input().split())
clauses = [ list(map(int, input().split())) for i in range(C) ]



def SAT(V, C, clauses):
    G, Greverse = constructionGraph(V, C, clauses)
    #print(G)
    SCC, componentNumber = findConnectedComponents(G, Greverse)
    #print(SCC)
    #print(componentNumber)
    for v in range(V):
        if componentNumber[v] == componentNumber[v+V]:
            print('UNSATISFIABLE')
            return
    print('SATISFIABLE')
    assignments = assignVariables(SCC, V)
    #print(assignments)
    for i in range(V):
        if assignments[i]==1:
            print(i+1, ' ', end='')
        else:
            print(-(i+1), ' ', end='')
    return



####################################################
# Construction of the graph
# and reverse Graph for SCC
###################################################

def constructionGraph(V, C, clauses):
    G = [None]*2*V
    Greverse = [None]*2*V
    for i in range(V):
        G[i] = []
        G[i+V] = []
        Greverse[i] = []
        Greverse[i+V] = []
    for c in clauses:
        if len(c) == 1:
            G[getIndexNegL(c[0])].append(getIndexL(c[0]))
            Greverse[getIndexL(c[0])].append(getIndexNegL(c[0]))
        else:
            G[getIndexNegL(c[0])].append(getIndexL(c[1]))
            G[getIndexNegL(c[1])].append(getIndexL(c[0]))
            Greverse[getIndexL(c[0])].append(getIndexNegL(c[1]))
            Greverse[getIndexL(c[1])].append(getIndexNegL(c[0]))
    return G, Greverse

def getIndexL(L):
    if L>0: 
        return L-1
    else:
        return abs(L)-1+V

def getIndexNegL(L):
    if L>0: 
        return L-1+V
    else:
        return abs(L)-1


############################################################
# find SCC
############################################################

def findConnectedComponents(G, Greverse):
    # indices goes from sink of G to source of G
    # so it is already the topological order of the SCC in reverse order
    indices = acyclic(Greverse)
    SCC, componentNumber = second(G, indices)
    return SCC, componentNumber

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
    SCC = []
    componentNumber = [None]*len(adj)
    visited2 = { k:False for k in range(len(adj))}
    # label is the number of Strongly connected component
    label = 0
    for v in indices:
        if not visited2[v]:
            SCC.append([])
            explore2(v, adj, visited2, SCC, label, componentNumber)
            label+=1
    return SCC, componentNumber

def explore2(v, adj, visited2, SCC, label, componentNumber):
    visited2[v] = True
    SCC[label].append(v)
    componentNumber[v] = label
    for w in adj[v]:
        if not visited2[w]:
            explore2(w, adj, visited2, SCC, label, componentNumber)



###############################################################
# assign variables
##############################################################
def assignVariables(SCC, V):
    assignments = [None]*2*V
    for C in SCC:
        if len(C)!=0 and assignments[C[0]]==None:
            for L in C:
                assignments[L]=1
                if L<V: assignments[L+V]=0
                else: assignments[L%V]=0
    return assignments


def main():
    SAT(V, C, clauses)

threading.Thread(target=main).start()



'''
# This solution tries all possible 2^n variable assignments.
# It is too slow to pass the problem.
# Implement a more efficient algorithm here.
def isSatisfiable():
    for mask in range(1<<n):
        result = [ (mask >> i) & 1 for i in range(n) ]
        formulaIsSatisfied = True
        for clause in clauses:
            clauseIsSatisfied = False
            if result[abs(clause[0]) - 1] == (clause[0] < 0):
                clauseIsSatisfied = True
            if result[abs(clause[1]) - 1] == (clause[1] < 0):
                clauseIsSatisfied = True
            if not clauseIsSatisfied:
                formulaIsSatisfied = False
                break
        if formulaIsSatisfied:
            return result
    return None

result = isSatisfiable()
if result is None:
    print("UNSATISFIABLE")
else:
    print("SATISFIABLE");
    print(" ".join(str(-i-1 if result[i] else i+1) for i in range(n)))
'''



