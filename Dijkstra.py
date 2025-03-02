def dijkstra(adj_matrix, source):
    n = len(adj_matrix)
    distances = [float('inf')] * n
    distances[source] = 0
    prev_nodes = [-1] * n  # To track shortest path
    visited = [False] * n  # Track visited nodes

    for _ in range(n):
        # Find the node with the smallest distance that hasn't been visited
        min_dist = float('inf')
        min_node = -1
        for i in range(n):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                min_node = i
        
        if min_node == -1:  # No more reachable nodes
            break
        
        visited[min_node] = True  # Mark node as visited

        # Update distances for neighbors
        for neighbor in range(n):
            weight = adj_matrix[min_node][neighbor]
            if weight > 0 and not visited[neighbor]:  # Ignore non-edges and visited nodes
                new_dist = distances[min_node] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    prev_nodes[neighbor] = min_node

    return distances, prev_nodes

def print_routing_table(distances, prev_nodes):
    print("Routing Table:")
    print("Node\tDistance\tPredecessor")
    for i, (dist, pred) in enumerate(zip(distances, prev_nodes)):
        print(f"{i}\t{dist}\t\t{pred}")

def get_shortest_path(prev_nodes, destination):
    path = []
    while destination != -1:
        path.append(destination)
        destination = prev_nodes[destination]
    return path[::-1]

# Example adjacency matrix
adj_matrix = [
    [0, 7, 0, 0, 0, 14],
    [7, 0, 9, 0, 0, 2],
    [0, 9, 0, 11, 0, 0],
    [0, 0, 11, 0, 6, 0],
    [0, 0, 0, 6, 0, 9],
    [14, 2, 0, 0, 9, 0]
]

source = 0  # Change as needed
destination = 4  # Change as needed

distances, prev_nodes = dijkstra(adj_matrix, source)
print_routing_table(distances, prev_nodes)
print("Shortest path:", get_shortest_path(prev_nodes, destination))