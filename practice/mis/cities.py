from graph import Node, WeightedEdge, Graph

# Step 1: Create nodes

toronto = Node("Toronto")
montreal = Node("Montreal")
ottawa = Node("Ottawa")

# Step 2: Create the graph
canada_map = Graph()

# Step 3: Add nodes to the Graph

canada_map.addNode(toronto)
canada_map.addNode(montreal)
canada_map.addNode(ottawa)

# Step 4: Create weighted edges (roads with distances)

road1 = WeightedEdge(toronto, montreal, 540)
road2 = WeightedEdge(montreal, ottawa, 200)
road3 = WeightedEdge(toronto, ottawa, 450)

# Step 5: Add edges to the graph

canada_map.addEdge(road1)
canada_map.addEdge(road2)
canada_map.addEdge(road3)

# Step 6: Print the graph

print(canada_map)
