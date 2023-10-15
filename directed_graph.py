# a base layer for a graph ig
# assume that all graphs are directed here

class Graph:
    # for more details about this see graph.md
    vertices_count = 0
    edges = []

    edge_list = []
    adj_matrix = []
    adj_list_in = []
    adj_list_out = []

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

        