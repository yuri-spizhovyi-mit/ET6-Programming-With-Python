import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Create a weighted directed graph
G = nx.DiGraph()

# Step 2: Add cities and distances (edges with weights)
edges = [
    ("Vancouver", "Calgary", 970),
    ("Calgary", "Regina", 750),
    ("Regina", "Winnipeg", 575),
    ("Winnipeg", "Thunder Bay", 705),
    ("Thunder Bay", "Ottawa", 1300),
    ("Ottawa", "Quebec", 450),
    ("Vancouver", "Edmonton", 1150),
    ("Edmonton", "Saskatoon", 525),
    ("Saskatoon", "Winnipeg", 780),
    ("Toronto", "Ottawa", 450),
    ("Toronto", "Montreal", 550),
    ("Montreal", "Quebec", 250),
    ("Calgary", "Winnipeg", 1200),
    ("Vancouver", "Toronto", 4200),
    ("Edmonton", "Winnipeg", 1300),
    ("Winnipeg", "Toronto", 2100),
    ("Ottawa", "Montreal", 200),
    ("Regina", "Toronto", 2800),
    ("Calgary", "Toronto", 3400),
    ("Saskatoon", "Toronto", 3100),
]

for src, dst, distance in edges:
    G.add_edge(src, dst, weight=distance)

# Step 3: Find the shortest path from Vancouver to Quebec using Dijkstra
start = "Vancouver"
end = "Quebec"

path = nx.dijkstra_path(G, source=start, target=end, weight="weight")
total_distance = nx.dijkstra_path_length(G, source=start, target=end, weight="weight")

print("🛣️ Shortest path (by distance):", " → ".join(path))
print("📏 Total distance:", total_distance, "km")

# Step 4: Visualize the graph

# Stable layout
# pos = nx.spring_layout(G, seed=42)

# Circle layout
# pos = nx.circular_layout(G)

# Shell layout
pos = nx.shell_layout(G)

# Kamada-Kawai layout (very clean for small graphs)
# pos = nx.kamada_kawai_layout(G)

# Draw all nodes and edges
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=1800,
    node_color="lightblue",
    font_size=10,
    arrowsize=20,
)

# Draw edge labels (distances)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(
    G, pos, edge_labels=edge_labels, font_size=8, label_pos=0.5
)

# Highlight the shortest path
if len(path) > 1:
    path_edges = list(zip(path[:-1], path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=3)

plt.title(f"Shortest Path from {start} to {end} ({total_distance} km)")
plt.tight_layout()
plt.show()
