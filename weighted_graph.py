import os
import codecs
import random

class WeightedGraph():
    '''Weighted graph data structure with advanced interface... hopefully'''

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
        assert len(self.nodes) > 2
        self.edges.append(edge)

    def create_random_node(self):
        # creates random 16 byte address
        identity = codecs.encode(os.urandom(16), 'hex').decode()
        # create random weight in a flat distribution 0-999
        weight = random.randint(0, 999)
        return (identity, weight)

    def create_random_edge(self):
        '''
            picks to random nodes and forms an edge between them
        '''
        # make sure there are at least 2 edges
        assert len(self.nodes) >= 2
        # temporary node list !!! mutable !!!
        temp_nodes = self.nodes
        # get one node from list
        position1 = random.randint(0, len(temp_nodes) - 1)
        node1 = temp_nodes[position1]
        temp_nodes.remove(node1)
        # get second node from list
        position2 = random.randint(0, len(temp_nodes) - 1)
        node2 = temp_nodes[position2]
        return (node1[0], node2[0])

### testing!

graph = WeightedGraph()
random_node1 = graph.create_random_node()
print('random_node1', random_node1)
graph.put_node(random_node1)
random_node2 = graph.create_random_node()
print('random_node2', random_node2)
graph.put_node(random_node2)
print('nodes', graph.nodes)
random_edge = graph.create_random_edge()
print('random_edge', random_edge)
