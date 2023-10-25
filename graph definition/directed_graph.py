# a base layer for a graph ig
# assume that all graphs are directed here

class Graph:
    # for more details about this see graph.md
    vertices_count = 0

    edge_list = []
    adj_matrix = []
    adj_list_incoming = []
    adj_list_outgoing = []

    # vertices - int - number of vertices in this graph (represented in whatever form)
    # edges - list - a list of pairs in the form (u, v) where u is the outgoing vertex and v is the incoming vertex for that edge - this list should be 0-indexed


    def __init__(self, vertices, edges):
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

    
    def add_edge(self, vertex_1, vertex_2):
        # assume that this is 0-indexed and the edge is from [vertex_1] => [vertex_2]


        self.edge_list.append((vertex_1, vertex_2))
        
        # outgoing array incoming edge
        self.adj_matrix[vertex_2][vertex_1] = 1

        self.adj_list_incoming[vertex_2].append(vertex_1) # yeah i could make this a binary sort and a binary list but that's for later
        self.adj_list_outgoing[vertex_1].append(vertex_2)

        return



    # "getter" methods - aka getting data
    def get_adj_matrix(self):
        return self.adj_matrix

    def get_adj_list(self):
        return self.adj_list_incoming, self.adj_list_outgoing
    
    def get_edge_list(self):
        return self.edge_list
    
    def get_vertices(self):
        return self.vertices_count
    
    
    # "setter" methods
    def add_vertex(self):

        # new vertex will essentially have the next numerical value


        self.vertices_count += 1

        # uh oh some messy graph stuff is going to happen
        # should i really optimize it?

        '''
        vertices = self.vertices_count
        self.adj_matrix = [[0]*vertices for _ in range(vertices)]

        for pair in edges:
            self.adj_matrix[pair[0]][pair[1]] = 1



        # adj_lists
        self.adj_list_incoming = [[] for i in range(vertices)]
        self.adj_list_outgoing = [[] for j in range(vertices)]

        for pair in edges:
            self.adj_list_incoming[pair[1]].append(pair[0])
            self.adj_list_outgoing[pair[0]].append(pair[1])
        '''


        # fix adj matrix
        self.adj_matrix.append([0]*(self.vertices_count - 1))
        for row in range(len(self.adj_matrix)):
            self.adj_matrix[row] = self.adj_matrix[row].append(0)
        
        self.adj_list_incoming.append([])
        self.adj_list_outgoing.append([])
        
        return
    

    
    # add vertex and edges
    def add_vertex_and_edges(self, vertex, edge_list):
        # edge_list is two lists
        # edge_list[0] is a list of incoming edges (think [0] => [new]) - simply a list of nodes
        # edge_list[1] is a list of outgoing edges ([new] => [k])

        self.add_vertex()
        
        for node in edge_list[0]:
            self.add_edge(node, self.vertices_count - 1)
        
        for node in edge_list[1]:
            self.add_edge(self.vertices_count - 1, node)
        
        # woohoo we're done


        



        

        