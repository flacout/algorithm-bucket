#Uses python3
import sys
import math

def clustering(x, y, k, n):
    # create a list of all weigthed edges.
    E=[]
    for v in range(n):
        for u in range(v+1, n):
            distance = math.sqrt((x[v]-x[u])**2 + (y[v]-y[u])**2)
            E.append( (distance, v, u))

    # create the data structures
    E.sort()
    dis_sets = [i for i in range(n)]
    ranks = [0 for i in range(n)]
    nb_sets = n

    for e in E:
        if find(e[1], dis_sets) != find(e[2], dis_sets):
            # when there is three sets, the next edge to be processed
            # is the shortest edge connecting the sets
            if nb_sets == k:
                return e[0]
            union(e[1], e[2], dis_sets, ranks)
            # the number of sets decrease by one at each unions
            nb_sets -=1


# find parent
def find(i, dis_sets):
    while dis_sets[i] != i:
        i = dis_sets[i]
    return dis_sets[i]

# union by rank
def union(i, j, dis_sets, rank):
    i_id = find(i,dis_sets)
    j_id = find(j,dis_sets)
    if i_id == j_id:
        return

    if rank[i_id] > rank[j_id]: 
        dis_sets[j_id] = i_id
    else :
        dis_sets[i_id] = j_id
        if rank[i_id] == rank[j_id]:
            rank[j_id] +=1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.12f}".format(clustering(x, y, k, n)))
