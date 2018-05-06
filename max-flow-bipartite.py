# python3
from queue import Queue

class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        #matching = [-1] * n

        graph = makeGraph(n,m,adj_matrix)
        matching = max_flow(graph, 0, graph.size() - 1, n)
        #busy_right = [False] * m
        #for i in range(n):
        #    for j in range(m):
        #        if adj_matrix[i][j] and matching[i] == -1 and (not busy_right[j]):
        #            matching[i] = j
        #            busy_right[j] = True
        return matching

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)



def makeGraph(n, m, adj_matrix):
    vertex_count = n+m+2
    graph = FlowGraph(vertex_count)
    # edge from source to flight
    for i in range(n):
        graph.add_edge(0, i+1, 1)
    # edge from crew to sink
    for i in range(m):
        graph.add_edge(n+i+1, n+m+1, 1)
    # internal edges
    for i in range(n):
        for j in range(m):
            if adj_matrix[i][j]==1:
                graph.add_edge(i+1, n+j+1, 1)
    return graph


def max_flow(graph, from_, to, n):
    while True:
        path, X = findPath(graph, from_, to)
        #print('path', path)
        if len(path)== 0 :
            return computeFlow(graph, n)
        #print('X', X)
        updateGraph(graph, X, path)

def computeFlow(graph, n):
    matching = [-1] * n
    #print('enter computeFlow()')
    # get edges_id of source node.
    for edge_id in graph.get_ids(0):
        edge = graph.get_edge(edge_id)
        if edge.flow==1:
            flight = edge.v
            for edge_id in graph.get_ids(flight):
                edge = graph.get_edge(edge_id)
                if edge.flow == 1:
                    vertex_crew = edge.v
                    matching[flight-1] = vertex_crew - n - 1
                    break

    return matching


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
