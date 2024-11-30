weight = [
    [0, 4, 0, 0],
    [0, 0, -2, 0],
    [0, 0, 0, 3],
    [0, 0, 0, 0],
]

n = 4  # Number of nodes
dist = [9999] * n  # Distance from the source to each node, initialized to a large number (infinity)
parent = [-1] * n  # Parent nodes, initially no parent for any node

source = 0  # Starting node (0th node)
dist[source] = 0  # Distance from the source to itself is 0

# Relaxation function that updates the distance and parent if a shorter path is found
def relax(u, v):
    if dist[v] > dist[u] + weight[u][v]:
        dist[v] = dist[u] + weight[u][v]
        parent[v] = u

# Bellman-Ford Algorithm
def BellmanFord():
    # Relax all edges n-1 times
    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if weight[u][v] != 0:  # Only consider edges with non-zero weights
                    relax(u, v)

    # Check for negative weight cycles
    for u in range(n):
        for v in range(n):
            if weight[u][v] != 0 and dist[v] > dist[u] + weight[u][v]:
                return False  # Negative weight cycle detected
    return True  # No negative weight cycle found

# Run the Bellman-Ford algorithm
if BellmanFord():
    print(f"Shortest distances from source {source}: {dist}")
    print(f"Parent nodes: {[p + 1 for p in parent]}")  # Parent nodes (adjusted for 1-based indexing)
else:
    print("Graph contains a negative weight cycle. No solution.")
