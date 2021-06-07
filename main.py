import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
#матриця суміжності
adj_matrix = np.matrix([[0, 8, 15, 10, 22, 15, 0, 0, 0, 0, 0, 0], 
[8, 0, 0, 22, 0, 0, 27, 0, 19, 0, 0, 0], 
[15, 0, 0, 0, 0, 30, 0, 14, 0, 0, 10, 0], 
[10, 22, 0, 0, 24, 0, 0, 0, 1, 0, 0, 0], 
[22, 0, 0, 24, 0, 14, 0, 0, 0, 20, 0, 0], 
[15, 0, 30, 0, 14, 0, 0, 0, 0, 0, 3, 0], 
[0, 27, 0, 0, 0, 0, 0, 0, 29, 2, 0, 26], 
[0, 0, 14, 0, 0, 0, 0, 0, 0, 13, 21, 24], 
[0, 19, 0, 1, 0, 0, 29, 0, 0, 4, 0, 21], 
[0, 0, 0, 0, 20, 0, 2, 13, 4, 0, 15, 27], 
[0, 0, 10, 0, 0, 3, 0, 21, 0, 15, 0, 23], 
[0, 0, 0, 0, 0, 0, 26, 24, 21, 27, 23, 0]])

G = nx.Graph(adj_matrix)
pos=nx.spring_layout(G)
nx.draw(G, pos,with_labels=True)

max_w_match = nx.max_weight_matching(G, maxcardinality=False, weight='weight')
Gr = nx.Graph()
Gr.add_edges_from(max_w_match)

labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
print("Максимальне зважене паросполучення", max_w_match)
nx.draw_networkx_nodes(Gr, pos, node_color='r')
nx.draw_networkx_edges(Gr,pos,edge_color='r', connectionstyle='arc3, rad = 0.3')

plt.show()