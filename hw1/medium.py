import ast
import networkx as nx
import matplotlib.pyplot as plt

with open('easy.py') as fs:
    source = fs.read()
    tree = ast.parse(source)

print(ast.dump(tree, indent=4))

G = nx.DiGraph()

for node in ast.walk(tree):
    G.add_node(node)

fig = plt.figure()
ax = plt.gca()
nx.draw(G, with_labels=True, ax=ax)
plt.show()