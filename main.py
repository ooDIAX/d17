import networkx as nx
from matplotlib import pyplot as plt


gr = nx.Graph()
num_edge = 6
gr.add_nodes_from([e + 1 for e in range(num_edge)])

gr.add_weighted_edges_from(
    [(1,2,1), (2,3,6), (3,6,2), 
     (1,4,1), (4,5,4), (5,6,6), (1,5,1)]
)

layout = nx.spring_layout(gr)

nx.draw(gr,pos = layout, with_labels = True)
nx.draw_networkx_edge_labels(gr, pos = layout, edge_labels=nx.get_edge_attributes(gr,'weight'))


# draw the minimum spanning tree in red


plt.savefig("imgs\Graph.png", format="PNG")
path = nx.dijkstra_path(gr, 1, num_edge)
path_edges = list(zip(path,path[1:]))
print("shortest path ", path)


nx.draw_networkx_nodes(gr,layout,nodelist=path,node_color='r')
nx.draw_networkx_edges(gr,layout,edgelist=path_edges,edge_color='r')
plt.savefig("imgs\ShortestPathGraph.png", format="PNG")
plt.show()
