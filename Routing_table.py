#README: An initial code which has a functional vertex and graph class built in order to store the input file in an easy-to-work-with data structure.Future work include completing Dijkstra algorithm and putting the pieces together.

import sys
INFINITY = sys.maxint
#Set number of elements that affect the link cost between nodes
element_num = 1

class Vertex:
    #Define a class vertex to hold a node
    def __init__ (self, id):
        self.id = id
        #Set the length value to INFINITY
        self.length_value = INFINITY
        self.visited = False
        #Use a dictionary to hold neighbors nodes
        self.neighbors  = {}
        #Initialize the predecessor of the node
        self.predecessor = None

    def add_neighbor(self, neighbor, weight):
        #Add a neighbor with given weight
        self.neighbors[neighbor] = weight

    def set_length_value(self, length):
        #Set the length value of the node
        self.length_value = length

    def set_visited(self):
        self.visited = True

    def set_predecessor(self,prev):
        self.predecessor = prev

    def get_id(self):
        return self.id

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]

    def get_length_value(self):
        return self.length_value

class Graph:
    #Define a Graph class that holds vertices
    def __init__(self):
        self.vertices = {}
        self.vert_count = 0

    def add_vertex(self, vertex_id):
        self.vert_count += 1
        node = Vertex(vertex_id)
        self.vertices[vertex_id] = node

    def add_edge(self, node1, node2, link_cost):
        if node1 not in self.vertices:
            self.add_vertex(node1)
        if node2 not in self.vertices:
            self.add_vertex(node2)

        self.vertices[node1].add_neighbor(self.vertices[node2], link_cost)
        self.vertices[node2].add_neighbor(self.vertices[node1], link_cost)

    def get_vertex(self, node):
        if node not in self.vertices:
            return None
        else:
            return self.vertices[node]

    def get_vertices(self):
        return self.vertices.keys()

def dijkstra():
    #Using Dijstra algorithm to create routing tables for entries
    return 0
def link_cost_calc():
    #Calculate the total weight of a link
    return 0
def input_process(filename):
    #Process the input and parse it into a data structure
    Network = Graph()
    fopen = open(filename,'r')
    for line in fopen:
        elem = line.strip("\n").split(" ")
        Network.add_edge(elem[0],elem[1],elem[2])
    return 0

def output():
    #Output the results into a file
    return 0

def main():
    input_process("test.dat")
    #Call main functions
    return 0
main()
