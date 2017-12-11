import os
import codecs
import random
import hashlib

class WeightedGraph():
    '''Weighted graph data structure with advanced interface... hopefully'''

    def __init__(self):
        self.nodes = []
        self.edges = []
        self.edge_space = []
        total_weight = 0

    def put_node(self, node):
        '''
            appends node/s to node list
            node is either a single edge tuple or list of tuples
        '''
        self.increase_edge_space(node)
        self.nodes.append(node)

    def put_edge(self, edge):
        '''
            appends edge/s to edge list
            edge is either a single edge tuple or list of tuples
        '''
        assert len(self.nodes) > 2
        self.edges.append(edge)

    def increase_edge_space(self, new_node):
        '''
            creates edge space for edge connections between new_node and existing nodes
        '''
        for node in self.nodes:
            edge_hash = self.get_permutation_hash(new_node, node)
            self.edge_space.append(edge_hash)

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

    def create_random_edges(self, num_edges):
        '''
            creates random edges
            edges is an integer value
        '''
        # make sure enough possible edges
        num_nodes = len(self.nodes)
        max_num_edges = num_nodes * (num_nodes - 1) / 2
        assert num_edges <= max_num_edges
        # temporary node list !!! mutable !!!
        temp_nodes = self.nodes
        for i in range(num_edges):
            position = random.randint(0, len(temp_nodes) - 1)
            node = temp_nodes[position]
            temp_nodes

    def get_permutation_hash(self, node1, node2):
        '''
            creates unique hash from two nodes
        '''
        # cannot form a permutation between the same node
        assert node1 != node2
        # alpha-numerical comparison of node hashes
        if node1[0] < node2[0]:
            concat_node = node2[0] + node1[0]
        else:
            concat_node = node1[0] + node2[0]
        return hashlib.sha256(concat_node.encode('utf8')).hexdigest()


### testing!

graph = WeightedGraph()
random_node1 = graph.create_random_node()
graph.put_node(random_node1)
random_node2 = graph.create_random_node()
graph.put_node(random_node2)
random_node3 = graph.create_random_node()
graph.put_node(random_node3)
print(graph.edge_space)
