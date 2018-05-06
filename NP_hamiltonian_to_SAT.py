# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]
#f = open('cl.txt', 'w')

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula():
    varMatrice, adj_matrix = processInput()
    printHeader(adj_matrix)

    printAllVertex(varMatrice)
    printPathOnce(varMatrice)
    printEachVertexOnce(varMatrice)
    printOnePositionOnPath(varMatrice)
    printedgeConnection(varMatrice, adj_matrix)



# path = nb vertices = n
# nb clauses n
# create adjacent matrix to spot the non egde
# create variables Vij for each vertex i in each position is the path j
def processInput():
    varMatrice = [[(p+v*n)+1 for p in range(n)] for v in range(n)]
    adj_matrix = [[0 for p in range(n)] for v in range(n)]
    for e in edges:
        adj_matrix[e[0]-1][e[1]-1] = 1
        adj_matrix[e[1]-1][e[0]-1] = 1
    #print(varMatrice)
    #print(adj_matrix)
    return varMatrice, adj_matrix


# nb var = n*n
def printHeader(adj_matrix):
    nb_ones=0
    for v in range(n):
        for u in range(n):
            if adj_matrix[v][u] == 1:
                nb_ones+=1
    nb_clauses = int(n*2  +  (n*(n-1)/2) *n*2  +  ((n*n)-n-nb_ones)*(n-1))
    nb_var = n*n
    print(str(nb_clauses)+' '+str(nb_var))
    #f.write('p cnf '+str(nb_var)+' '+str(nb_clauses)+'\n')
    return


#####################################################################
# CLAUSES
####################################################################

# clause all vertex are on the path
# nb clauses(n*(n-1)/2) *n
# (V1p V1p ...) for all p
def printAllVertex(varMatrice):
    #print("all vetex on path")
    for v in range(n):
        clause =''
        for p in range(n):
            clause += str(varMatrice[v][p])+' '
        print(clause+'0')
        #f.write(clause+' 0'+'\n')
    return

# clause all position must be on the path
# (Vv1 Vv2 ...) for all vertex
def printPathOnce(varMatrice):
    #print("each path at least once")
    for p in range(n):
        clause =''
        for v in range(n):
            clause += str(varMatrice[v][p])+' '
        print(clause+'0')
        #f.write(clause+' 0'+'\n')
    return


# clause each vertex is visited only once
# nb clauses(n*(n-1)/2) *n
# combinaison of two p
# (!V1p1 !V1p2)(!V1p1 !V1p3)(!V1p1 !V1p4)
# (!V1p2 !V1p3)(!V1p2 !V1p4)
# (!V1p3 !V1p4)
# if V1p1 and V1p2 are the same then (vertex two path position)CNF = false
def printEachVertexOnce(varMatrice):
    #print("each vertex visit once")
    for v in range(n):
        #print("new vertex")
        for p in range(n-1):
            for stop in range(p+1,n):
                clause = '-'+str(varMatrice[v][p])+' '+'-'+str(varMatrice[v][stop])
                print(clause+' 0')
                #f.write(clause+' 0'+'\n')
    return

# there is only one vertex on each position in the path
# combinaison of two v
# (!V1p1 !V2p1)(!V1p1 !V3p1)(!V1p1 !V4p1)
# (!V2p1 !V3p1)(!V2p1 !V4p1)
# (!V3p1 !V4p1)
# if V1p1 !V2p1 are the same then (2 vertex on same path position) CNF = false
def printOnePositionOnPath(varMatrice):
    #print("one vertex on each position")
    for p in range(n):
        #print("new path")
        for v in range(n-1):
            for stop in range(v+1,n):
                clause = '-'+str(varMatrice[v][p])+' '+'-'+str(varMatrice[stop][p])
                print(clause+' 0')
                #f.write(clause+' 0'+'\n')
    return


# clause two successive vertex must be connected by an edge
# OR non edge pair of vertex are non on a successive path
# nb path = n-1
# nb no edge = (n*n) - n(diagonal) - nb_edges*2
# for each non edge in the adj_matrix
# check if it is on one of the path
# non edge V1 V2
# (!V1p1 !V2p2) (!V1p2 !V2p3) (!V1p3 !V2p4)
def printedgeConnection(varMatrice, adj_matrix):
    #print("adjacent vertex in path")
    paths = [[i,i+1] for i in range(n-1)]

    # for par of vertex not connected by an edge
    for v in range(n):
        for u in range(n):
            if (adj_matrix[v][u] == 0) and (v!=u):
                #print("one vertex")
                for p in paths:
                    clause = '-'+str(varMatrice[v][p[0]])+' '+'-'+str(varMatrice[u][p[1]])
                    print(clause+' 0')
                    #f.write(clause+' 0'+'\n')
    return



##########################
# MAIN
############################
printEquisatisfiableSatFormula()
#f.close()
