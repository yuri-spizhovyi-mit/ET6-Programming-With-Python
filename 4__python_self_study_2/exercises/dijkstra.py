import heapq

def dijkstra(graph, start):
    # Initialize data structures
    shortest_distances = {node: float('inf') for node in graph}  # Tentative distances
    shortest_distances[start] = 0  # Distance to the source is 0
    priority_queue = [(0, start)]  # Priority queue for processing nodes (distance, node)
    previous_nodes = {node: None for node in graph}  # For path reconstruction

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)  # Get the node with the smallest distance

        # Skip if we've already processed this node with a smaller distance
        if current_distance > shortest_distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight  # Calculate tentative distance
            if distance < shortest_distances[neighbor]:  # Update if smaller distance found
                shortest_distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))  # Add to the priority queue

    return shortest_distances, previous_nodes

def reconstruct_path(previous_nodes, start, end):
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    return path[::-1]  # Reverse the path to get start-to-end order

# Example Graph
graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 5},
    'D': {'B': 1, 'C': 5, 'E': 3},
    'E': {'D': 3}
}

# Test the algorithm
start_node = 'A'
end_node = 'E'
shortest_distances, previous_nodes = dijkstra(graph, start_node)
shortest_path = reconstruct_path(previous_nodes, start_node, end_node)

# Output the results
print(f"Shortest distances from {start_node}: {shortest_distances}")
print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")
