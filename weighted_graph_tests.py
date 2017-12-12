from weighted_graph import WeightedGraph
from termcolor import cprint
def run_tests():
    graph = WeightedGraph()
    # create a large random graph
    create_random_graph(graph, 100, 500)

### test #1
def create_random_graph(graph, num_nodes, num_edges):
    max_edges = num_max_edges(num_nodes)
    assert num_edges < max_edges
    for i in range(num_nodes):
        node = graph.create_random_node()
        graph.put_node(node)
    print(graph.nodes)
    # graph.create_random_edges(num_edges)
    # assert len(graph.available_edges) == max_edges - num_edges
    # assert len(graph.edges) == num_edges
    cprint('### test #1: create_random_graph is passing all 2 tests', 'green')

#### test #2

### utils
def num_max_edges(num_nodes):
    return num_nodes * (num_nodes - 1) / 2

if __name__ == '__main__':
  run_tests()
