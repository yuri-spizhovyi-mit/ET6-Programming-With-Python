import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add edges (this also adds the nodes automatically)
G.add_edge("Toronto", "Montreal")
G.add_edge("Toronto", "Ottawa")
G.add_edge("Montreal", "Quebec")
G.add_edge("Ottawa", "Quebec")

# Create a layout for the nodes
pos = nx.spring_layout(G)  # You can also try: nx.shell_layout(G)

# Draw the nodes and edges
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=2000,
    font_size=12,
    arrows=True,
    arrowstyle="->",
    arrowsize=20,
)

# Optionally draw edge labels (if you want to add weights later)
# edge_labels = {("Toronto", "Montreal"): "540km"}
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("City Graph (Directed)")
plt.show()
