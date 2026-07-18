import heapq
import time

# ---------------- Dijkstra Algorithm ----------------
def dijkstra(graph, source):
    """
    Dijkstra's Algorithm using Min-Heap
    Time Complexity : O((V + E) log V)
    Space Complexity: O(V)
    """

    n = len(graph)

    dist = [float('inf')] * n
    prev = [None] * n

    dist[source] = 0

    pq = [(0, source)]
    visited = set()

    while pq:

        current_distance, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        for v, weight in graph[u]:

            if dist[u] + weight < dist[v]:

                dist[v] = dist[u] + weight
                prev[v] = u

                heapq.heappush(pq, (dist[v], v))

    return dist, prev, len(visited)


# ---------------- Path Reconstruction ----------------
def reconstruct_path(prev, source, target):

    path = []

    while target is not None:
        path.append(target)
        target = prev[target]

    path.reverse()

    if path and path[0] == source:
        return path

    return []


# ---------------- Display Graph ----------------
def display_graph(graph):

    print("\nGraph (Adjacency List):")

    for vertex in graph:
        print(f"{vertex} -> {graph[vertex]}")


# ---------------- Main Program ----------------
graph = {

    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: [(5, 2)],
    5: []

}

display_graph(graph)

vertices = len(graph)

edges = sum(len(graph[v]) for v in graph)

print("\nTotal Vertices :", vertices)
print("Total Edges    :", edges)

# User Input
while True:
    try:
        source = int(input(f"\nEnter Source Vertex (0-{vertices-1}): "))

        if source in graph:
            break
        else:
            print("Invalid Vertex! Try Again.")

    except ValueError:
        print("Please enter a valid integer.")

# Start Timer
start_time = time.perf_counter()

dist, prev, visited = dijkstra(graph, source)

# End Timer
end_time = time.perf_counter()

execution_time = end_time - start_time

# ---------------- Output ----------------
print("\nShortest Paths from Vertex", source)

print("-" * 75)
print(f'{"Vertex":<10}{"Distance":<12}{"Shortest Path"}')
print("-" * 75)

for v in range(vertices):

    path = reconstruct_path(prev, source, v)

    if path:
        path_str = " -> ".join(map(str, path))
    else:
        path_str = "No Path"

    distance = dist[v] if dist[v] != float('inf') else "INF"

    print(f"{v:<10}{distance!s:<12}{path_str}")

print("-" * 75)

print("\nSummary")
print("-------")
print("Visited Vertices :", visited)
print("Execution Time   : {:.8f} seconds".format(execution_time))

print("\nAlgorithm Completed Successfully.")
