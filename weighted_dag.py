import os
import codecs
import random

class WeightedDag():
    '''Weighted daga data strcuture with interface and graphing tool'''

    #### DATA STRUCTURE

    def __init__(self):
        # nodes are flat set
        self.nodes = {}

    #### INTERFACE

    def put_root(self, node):
        self.nodes.add()

    ### UTILS

    def create_random_root(self):
        id = self.create_id()
        weight = self.random_weight()
        return (id, weight)

    def create_id(self):
        return codecs.encode(os.urandom(16), 'hex').decode()

    def random_weight(self):
        return random.randint(0, 999)

### testing!
graph = WeightedDag()
root1 = graph.create_random_root()
print(root1)
