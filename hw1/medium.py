import ast
import inspect
import networkx as nx
import matplotlib.pyplot as plt

from easy import fib


def travel_ast(node, labels,  graph):
    graph.add_node(node)
    labels.update({node: node.__class__.__name__})

    for child in ast.iter_child_nodes(node):
        # print(f'{node}:{child}')
        graph.add_edge(node, child)
        travel_ast(child, labels, graph)

def create_ast_graph(func):
    tree = ast.parse(inspect.getsource(func))
    graph = nx.DiGraph()
    label_map = {}

    travel_ast(tree, label_map, graph)
    return graph, label_map

graph, label_map = create_ast_graph(fib)

pos = nx.spring_layout(graph, k=1, seed=1)
nx.draw(graph, labels=label_map, with_labels=True)
plt.savefig("hw1/artifacts/1.png")