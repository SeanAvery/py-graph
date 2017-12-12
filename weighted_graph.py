import os
import codecs
import random
import hashlib
import plotly
from plotly.offline import iplot, plot
from plotly.graph_objs import Scatter, Layout, Marker, Line, Data, Figure

class WeightedGraph():
    '''Weighted graph data structure with advanced interface... hopefully'''

    def __init__(self):
        self.nodes = []
        self.edges = []
        self.edge_space = []
        self.available_edges = []
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
        self.available_edges.remove(edge)

    def increase_edge_space(self, new_node):
        '''
            creates edge space for edge connections between new_node and existing nodes
        '''
        for node in self.nodes:
            edge_hash = self.get_permutation_hash(new_node, node)
            new_edge = (edge_hash, new_node[0], node[0])
            self.edge_space.append(new_edge)
            self.available_edges.append(new_edge)

    def create_random_node(self):
        # creates random 16 byte address
        identity = codecs.encode(os.urandom(16), 'hex').decode()
        # create random weight in a flat distribution 0-999
        weight = random.randint(0, 999)
        return (identity, weight)

    def create_random_edges(self, num_edges):
        '''
            creates random edges
            num_edges is an integer value
        '''
        assert len(self.nodes) >= 2
        assert num_edges <= len(self.available_edges)
        for _ in range(num_edges):
            new_edge = random.choice(self.available_edges)
            self.put_edge(new_edge)

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

    def plot_graph(self):
        x_coordinates = []
        y_coordinates = []
        for node in self.nodes:
            x_coordinates.append(random.randint(0, 99))
            y_coordinates.append(random.randint(0, 99))

        node_trace = Scatter(
            x = x_coordinates,
            y = y_coordinates,
            mode = 'markers'
        )

        edge_trace = Scatter(
            x=[],
            y=[],
            line=Line(width=1.0,color='#A9A9A9'),
            hoverinfo='none',
            mode='lines')
        print(self.nodes)

        for edge in self.edges:
            node1 = [node for node in self.nodes if edge[1] in node]
            index1 = self.nodes.index(node1[0])
            x0 = x_coordinates[index1]
            y0 = y_coordinates[index1]
            node2 = [node for node in self.nodes if edge[1] in node]
            index2 = self.nodes.index(node2[0])
            x1 = x_coordinates[index2]
            y1 = y_coordinates[index2]
            edge_trace['x'] += [x0, x1, None]
            edge_trace['y'] += [y0, y1, None]


            fig = Figure(data=Data([edge_trace, node_trace]),
                layout=Layout(
                title='<br>Network graph made with Python',
                titlefont=dict(size=16),
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))

            plotly.offline.plot(fig, )



### testing!
#
# graph = WeightedGraph()
# random_node1 = graph.create_random_node()
# graph.put_node(random_node1)
# random_node2 = graph.create_random_node()
# graph.put_node(random_node2)
# random_node3 = graph.create_random_node()
# graph.put_node(random_node3)
# print(graph.edge_space)
