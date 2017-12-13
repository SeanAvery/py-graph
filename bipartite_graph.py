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

    def put_edge(self, edge):
        '''
            append to edge ledger
            remove from available_edges
        '''
        assert len(self.nodes[0]) > 0 and len(self.nodes[1]) > 0
        self.edges.append(edge)
        self.available_edges.remove(edge)

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

    def create_random_nodes(self, num_nodes):
        for _ in range(num_nodes):
            new_node = self.create_random_node()
            side = random.getrandbits(1)
            self.put_node(new_node, side)

    def create_random_edges(self, num_edges):
        assert num_edges <= len(self.available_edges)
        for _ in range(num_edges):
            new_edge = random.choice(self.available_edges)
            self.put_edge(new_edge)

### testing!
graph = BipartiteGraph()
graph.create_random_nodes(10)
graph.create_random_edges(30)
print(graph.nodes)
print(graph.edges)
