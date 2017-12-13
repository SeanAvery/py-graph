import os
import codecs
import random

class WeightedDag():
    '''Weighted Directed Acyclic Graph data strcuture with interface and graphing tool'''

    #### DATA STRUCTURE

    def __init__(self):
        # nodes are flat set
        self.nodes = set()
        self.roots = set()
        self.leaves = set()

    #### INTERFACE

    def put_root(self, node):
        self.nodes.add(node)
        self.roots.add(node)

    def put_leaf(self, node):
        parent = next((x for x in self.leaves if x[0]== node[0]), None)
        if parent in self.leaves:
            self.leaves.remove(parent)
        self.nodes.add(node)
        self.leaves.add(node)

    ### UTILS

    def create_random_root(self):
        id = self.create_id()
        weight = self.random_weight()
        return (None, id, weight)

    def create_random_leaf(self):
        parent = random.choice(tuple(self.nodes))
        id = self.create_id()
        weight = self.random_weight()
        return (parent[1], id, weight)

    def create_id(self):
        return codecs.encode(os.urandom(16), 'hex').decode()

    def random_weight(self):
        return random.randint(0, 999)

### testing!
graph = WeightedDag()
root1 = graph.create_random_root()
graph.put_root(root1)
leaf1 = graph.create_random_leaf()
graph.put_leaf(leaf1)
leaf2 = graph.create_random_leaf()
graph.put_leaf(leaf2)
print(graph.nodes)
print(graph.leaves)
