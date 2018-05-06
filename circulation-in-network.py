# python3
from queue import Queue

class MaxMatching:
    def __init__(self):
        self.V = 0
        self.E = 0
        self.OUT = []
        self.IN = []
        self.lowerBond = []

    def read_data(self):
        self.V, self.E = map(int, input().split())
        self.OUT = [0 for i in range(self.V)]
        self.IN = [0 for i in range(self.V)]  
        vertex_count = self.V+2
        graph = FlowGraph(vertex_count)
        # add edges from input()
        for i in range(self.E):
            fro, to, low, cap = map(int, input().split())
            graph.add_edge(fro-1, to-1, cap-low)
            # add lower bond to out[from] and in[to]
            self.OUT[fro-1] += low
            self.IN[to-1] += low
            self.lowerBond.append(low) 
        #print(self.OUT)
        #print(self.IN)

        # add edges cap:IN[v] from Source to all vertex Source is self.V index
        # add edges cap:OUT[v] from all vertex to Sink with index self.V+1
        for v in range(self.V):
            graph.add_edge(self.V, v, self.IN[v])
            graph.add_edge(v, self.V+1, self.OUT[v])
        return graph

    def write_response(self, graph):
        for i, bond_edge in enumerate(self.lowerBond):
            # edges in graph are stoded in double 
            circulation = graph.edges[i*2].flow + bond_edge
            #print('edge flow '+str(graph.edges[i*2].flow), 'edge bond '+str(bond_edge))
            print(circulation)

    def solve(self):
        graph = self.read_data()
        maxFlow = max_flow(graph, self.V, self.V+1)
        #print(maxFlow)
        if maxFlow == sum (self.OUT):
            print('YES')
            self.write_response(graph)
        else:
            print('NO')
            return


def max_flow(graph, from_, to):
    flow = 0 
    while True:
        path, X = findPath(graph, from_, to) 
        #print('path', path)
        if len(path)== 0 : 
            return computeFlow(graph, from_)
        #print('X', X)
        updateGraph(graph, X, path)
        #print('flow', flow)

def computeFlow(graph, source):
    flow = 0
    # get edges_id of source node.
    for edge_id in graph.get_ids(source):
        # forward (even) case only
        if (edge_id%2==0):
            edge = graph.get_edge(edge_id)
            flow += edge.flow
    return flow


######################################################
# MAX-FLOW
######################################################

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        #forward_edge = Edge(from_, to, capacity)
        #backward_edge = Edge(to, from_, 0)
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, capacity)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        # get edges id in the self.edge list
        return self.graph[from_]

    def get_edge(self, id):
        # return one edge from a vertex.
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        # ^ is bitwise XOR
        # x^1 is x-1 if x odd(impair)     x+1 if x even(pair)
        self.edges[id].flow += flow   # forward edge
        self.edges[id ^ 1].flow -= flow # 




###########################################################
# BFS
###########################################################
def findPath(graph, from_, to):
    #print('enter findPath()')
    tree = BFS(graph, from_, to)
    #print("tree", tree)
    if tree[to] == None : 
        return [],0
    path, X = reconstructPath(from_, to, tree, graph)
    #print("path", path)
    return path, X

def reconstructPath(from_, to, tree, graph):
    # construct path
    # find minimum value
    min_value = float('inf')
    path = []
    while to!=from_:
        # path contain edges_id
        edge_id = tree[to][1]
        edge = graph.get_edge(edge_id)
        # forward (even) case
        if (edge_id%2==0) and ((edge.capacity - edge.flow) < min_value):
            min_value = edge.capacity - edge.flow
        # backward (odd) case cap + flow = cap + (negative value)
        if (edge_id%2!=0) and (-edge.flow < min_value):
            min_value = -edge.flow
        path.append(edge_id)
        to = tree[to][0]

    return path, min_value

def BFS(graph, from_, to):
    dist = [-1 for _ in range(graph.size())]
    prev = [None for _ in range(graph.size())]
    dist[from_] = 0
    q = Queue()
    q.put(from_)

    while (not q.empty()):
        u = q.get()
        for edge_id in graph.get_ids(u):
            edge = graph.get_edge(edge_id)
            # forward (even) case
            # edge.flow has to be inferior to capacity.
            if (edge_id%2==0) and (dist[edge.v] == -1) and (edge.flow < edge.capacity):
                q.put(edge.v)
                dist[edge.v] = dist[u] + 1
                prev[edge.v]= (u, edge_id)
                # stop when reach the sink
                if edge.v==to:
                    return prev
            # backward (odd) case
            # edge.flow has to be inferior to 0.
            elif (edge_id%2!=0) and (dist[edge.v] == -1) and (edge.flow < 0):
                q.put(edge.v)
                dist[edge.v] = dist[u] + 1
                prev[edge.v]=(u, edge_id)
                # stop when reach the sink
                if edge.v==to:
                    return prev
    return prev


#######################################################
# update graph edges along the path with value of flow
########################################################

def updateGraph(graph, min_value, path):
    #print('enter updateGraph')
    for edge_id in path:
        graph.add_flow(edge_id, min_value)
    return





if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
