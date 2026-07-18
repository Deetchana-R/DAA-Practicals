import heapq
import time

# ---------------- Union Find ----------------
class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True


# ---------------- Kruskal ----------------
def kruskal(n, edges):

    edges = sorted(edges)

    uf = UnionFind(n)

    mst = []
    total_cost = 0

    for weight, u, v in edges:

        if uf.union(u, v):

            mst.append((u, v, weight))
            total_cost += weight

            if len(mst) == n - 1:
                break

    return mst, total_cost


# ---------------- Prim ----------------
def prim(n, graph, start):

    visited = [False] * n

    parent = [-1] * n

    key = [float("inf")] * n

    key[start] = 0

    pq = [(0, start)]

    mst = []

    total_cost = 0

    while pq:

        weight, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        if parent[u] != -1:
            mst.append((parent[u], u, weight))
            total_cost += weight

        for v, wt in graph.get(u, []):

            if not visited[v] and wt < key[v]:

                key[v] = wt
                parent[v] = u

                heapq.heappush(pq, (wt, v))

    return mst, total_cost


# ---------------- Graph ----------------

n = 7

edges = [
    (7, 0, 1),
    (5, 0, 3),
    (8, 1, 2),
    (9, 1, 3),
    (7, 1, 4),
    (5, 2, 4),
    (15, 3, 4),
    (6, 3, 5),
    (8, 4, 5),
    (9, 4, 6),
    (11, 5, 6)
]

graph = {}

for w, u, v in edges:

    graph.setdefault(u, []).append((v, w))
    graph.setdefault(v, []).append((u, w))


print("========== MINIMUM SPANNING TREE ==========")

print("\nGraph Edges")

for w, u, v in edges:
    print(f"{u} -- {v}  Weight = {w}")

print("\nTotal Vertices :", n)
print("Total Edges    :", len(edges))

start_vertex = int(input("\nEnter starting vertex for Prim's Algorithm: "))

# Kruskal
start = time.perf_counter()

kruskal_mst, kruskal_cost = kruskal(n, edges)

kruskal_time = (time.perf_counter() - start) * 1000

# Prim
start = time.perf_counter()

prim_mst, prim_cost = prim(n, graph, start_vertex)

prim_time = (time.perf_counter() - start) * 1000


print("\n========== KRUSKAL MST ==========")

for u, v, w in kruskal_mst:
    print(f"{u} -- {v}   Weight = {w}")

print("Total Cost :", kruskal_cost)

print("\n========== PRIM MST ==========")

for u, v, w in prim_mst:
    print(f"{u} -- {v}   Weight = {w}")

print("Total Cost :", prim_cost)

print("\n========== PERFORMANCE ==========")

print("Kruskal Time : {:.6f} ms".format(kruskal_time))
print("Prim Time    : {:.6f} ms".format(prim_time))

print("\nVerification")

if kruskal_cost == prim_cost:
    print("✔ Both algorithms produced the SAME MST cost.")
else:
    print("✘ MST costs are different.")

print("\nNumber of MST Edges :", len(kruskal_mst))

print("\nTime Complexity")
print("Kruskal : O(E log E)")
print("Prim    : O(E log V)")

print("\nProgram Executed Successfully.")
