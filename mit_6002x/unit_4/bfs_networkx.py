import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Create directed graph
G = nx.DiGraph()

# Step 2: Add edges (automatically adds the nodes)
G.add_edge("Toronto", "Montreal")
G.add_edge("Toronto", "Ottawa")
G.add_edge("Montreal", "Quebec")
G.add_edge("Ottawa", "Quebec")

# Step 3: Find shortest path using BFS
start = "Toronto"
end = "Quebec"

try:
    path = nx.shortest_path(G, source=start, target=end)
    print("🛣️ Shortest path:", " → ".join(path))
except nx.NetworkXNoPath:
    print("🚫 No path found between", start, "and", end)
    path = []

# Step 4: Draw graph
pos = nx.spring_layout(G)

# Draw all nodes and edges
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=2000,
    font_size=12,
    arrows=True,
    arrowsize=20,
)

# Step 5: Highlight the path
if path and len(path) > 1:
    edge_list = list(zip(path[:-1], path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color="red", width=2.5)

plt.title(f"BFS Path from {start} to {end}")
plt.show()
