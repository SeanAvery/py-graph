import os
import codecs
import random

class BipartiteGraph():
    '''Birtate grage datastructure, interface, and max flow algorithms'''

    def __init__(self):
        self.nodes = ([], [])
        # directed edges
        self.edges = []
        self.edge_space = []
        self.available_edges = []

    def put_node(self, node, side):
        '''
            account for edge spae increase
            add node to partite set
        '''
        self.increase_edge_space(node, 1 - side)
        self.nodes[side].append(node)

    def increase_edge_space(self, node, side):
        '''
            creates new potential edge connetions
        '''
        for n in self.nodes[side]:
            self.edge_space.append((node[0], n[0]))
            self.available_edges.append((node[0], n[0]))
            self.edge_space.append((n[0], node[0]))
            self.available_edges.append((n[0], node[0]))


    def create_random_node(self):
        # creates random 16 byte address (unique identifier)
        identity = codecs.encode(os.urandom(16), 'hex')
        # create random weight score 0-999
        weight = random.randint(0, 999)
        return (identity, weight)

### testing!
graph = BipartiteGraph()
node1 = graph.create_random_node()
graph.put_node(node1, 0)
node2 = graph.create_random_node()
graph.put_node(node2, 1)
print(graph.nodes)
print(graph.edge_space)
