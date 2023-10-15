# a base layer for a graph ig
# assume that all graphs are directed here

class Graph:
    # for more details about this see graph.md
    vertices_count = 0
    edges = []

    edge_list = []
    adj_matrix = []
    adj_list_incoming = []
    adj_list_outgoing = []

    # vertices - int - number of vertices in this graph (represented in whatever form)
    # edges - list - a list of pairs in the form (u, v) where u is the outgoing vertex and v is the incoming vertex for that edge - this list should be 0-indexed


    def __init__(self, vertices, edges):
        self.edges = edges
        self.vertices_count = vertices

        # generate everything else
        self.edge_list = edges

        
        # adj matrix
        # generate VxV matrix of 0s
        self.adj_matrix = [[0]*vertices for _ in range(vertices)]

        for pair in edges:
            self.adj_matrix[pair[0]][pair[1]] = 1



        # adj_lists
        self.adj_list_incoming = [[] for i in range(vertices)]
        self.adj_list_outgoing = [[] for j in range(vertices)]

        for pair in edges:
            self.adj_list_incoming[pair[1]].append(pair[0])
            self.adj_list_outgoing[pair[0]].append(pair[1])
    
    
    def print_out(self):
        print(self.edge_list)
        print(self.adj_matrix)
        print(self.adj_list_incoming)
        print(self.adj_list_outgoing)



        