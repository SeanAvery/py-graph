import os
import codecs
import random

class WeightedGraph():
    """Weighted graph data structure with advanced interface... hopefully"""
    def __init__(self):
        self.nodes = []
        self.edges = []
        total_weight = 0

    def put_node(self, node):
        '''
            appends node/s to node list
            node is either a single edge tuple or list of tuples
        '''
        self.nodes.append(node)

    def put_edge(self, edge):
        '''
            appends edge/s to edge list
            edge is either a single edge tuple or list of tuples
        '''
        self.edges.append(edge)

def create_random_node():
    # creates random 16 byte address
    identity = codecs.encode(os.urandom(16), 'hex').decode()
    # create random weight in a flat distribution 0-999
    weight = random.randint(0, 999)
    return (identity, weight)

def create_random_edge():
    '''
        picks to random nodes and forms an edge between them
    '''

graph = Graph()
node1 = ('edge1')
graph.put_node(node1)
edge1 = ('edge1')
graph.put_edge(edge1)
random_node = create_random_node()
print(random_node)
