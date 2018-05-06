# python3
# Reduction to SAT
# the file output is to use with my minisat solver
# for which the format is a little different from the grader

n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]
#f = open('cl.txt', 'w')

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula():
    printHeader()
    for v in range(n):
        printVertexClause(v)
    for e in edges:
        printEdgeClause(e)



def printHeader():
    nb_clauses = n+m*3
    nb_var = n*3
    print(str(nb_clauses)+' '+str(nb_var))
    #f.write('p cnf '+str(nb_var)+' '+str(nb_clauses)+'\n')

# clause each vertex has to be colored by some color
# vertex nb from 1 to ...n
# color 1 to 3
# CNF (V11 V12 V13)(V21 V22 V23)...(Vn1 Vn2 Vn3)
def printVertexClause(v):
    col1 = (v*3)+1
    col2 = (v*3)+2
    col3 = (v*3)+3
    print(str(col1)+' '+str(col2)+' '+str(col3)+' 0')
    f.write(str(col1)+' '+str(col2)+' '+str(col3)+' 0'+'\n')


# clause vertices connected by an edge must have different colors
# CNF (!Vu1 !Vv1)(!Vu2 !Vv2)(!Vu3 !Vv3)
# CNF true if all term in parentesis are different
# if same color: (!1 !1)=0  = false CNF
def printEdgeClause(e):
    # variable Vij for each vertex i color j
    # access variable number by multiplying index by 3
    vi = ((e[0]-1)*3)
    ei = ((e[1]-1)*3)
    print('-'+str(vi+1)+' -'+str(ei+1)+' 0')
    print('-'+str(vi+2)+' -'+str(ei+2)+' 0')
    print('-'+str(vi+3)+' -'+str(ei+3)+' 0')
    f.write('-'+str(vi+1)+' -'+str(ei+1)+' 0'+'\n')
    f.write('-'+str(vi+2)+' -'+str(ei+2)+' 0'+'\n')
    f.write('-'+str(vi+3)+' -'+str(ei+3)+' 0'+'\n')




#################
# MAIN
#################
printEquisatisfiableSatFormula()
f.close()
