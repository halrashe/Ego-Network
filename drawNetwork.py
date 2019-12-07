import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g = nx.read_edgelist('filename.txt')

print len(g)
print 'avg path length ' + str(nx.average_shortest_path_length(g))
print 'avg clustering ' + str(nx.average_clustering(g))
print 'is the graph connected? ' + str(nx.is_connected(g))
print 'diam = ' + str(nx.diameter(g))

nx.draw(g, with_labels=False, node_size=7)
plt.show()
