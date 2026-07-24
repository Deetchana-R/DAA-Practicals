from itertools import permutations

INF = float('inf')

# -------------------------------------------------
# Reduce Cost Matrix
# -------------------------------------------------
def reduce_matrix(matrix):
    n = len(matrix)
    reduced = [row[:] for row in matrix]
    reduction_cost = 0

    # Row Reduction
    for i in range(n):
        row_min = min(reduced[i])
        if row_min != INF and row_min > 0:
            reduction_cost += row_min
            for j in range(n):
                if reduced[i][j] != INF:
                    reduced[i][j] -= row_min

    # Column Reduction
    for j in range(n):
        col_min = min(reduced[i][j] for i in range(n))
        if col_min != INF and col_min > 0:
            reduction_cost += col_min
            for i in range(n):
                if reduced[i][j] != INF:
                    reduced[i][j] -= col_min

    return reduced, reduction_cost


# -------------------------------------------------
# TSP using Brute Force (Verification)
# -------------------------------------------------
def tsp(cost_matrix):
    n = len(cost_matrix)
    vertices = list(range(1, n))

    minimum_cost = INF
    best_route = []

    for path in permutations(vertices):
        route = [0] + list(path) + [0]

        current_cost = 0
        for i in range(n):
            current_cost += cost_matrix[route[i]][route[i + 1]]

        if current_cost < minimum_cost:
            minimum_cost = current_cost
            best_route = route

    return best_route, minimum_cost


# -------------------------------------------------
# Display Matrix
# -------------------------------------------------
def display_matrix(matrix, names):
    print("\nCost Matrix")
    print("-" * 40)

    print("     ", end="")
    for city in names:
        print(f"{city:>6}", end="")
    print()

    for i in range(len(matrix)):
        print(f"{names[i]:>4}", end="")
        for value in matrix[i]:
            if value == INF:
                print(f"{'INF':>6}", end="")
            else:
                print(f"{value:>6}", end="")
        print()


# -------------------------------------------------
# Main Program
# -------------------------------------------------

cost = [
    [INF, 10, 8, 9, 7],
    [10, INF, 10, 5, 6],
    [8, 10, INF, 8, 9],
    [9, 5, 8, INF, 6],
    [7, 6, 9, 6, INF]
]

cities = ['A', 'B', 'C', 'D', 'E']

display_matrix(cost, cities)

reduced_matrix, reduction_cost = reduce_matrix(cost)

print("\nReduced Cost Matrix")
print("-" * 40)
display_matrix(reduced_matrix, cities)

print(f"\nInitial Reduction Cost = {reduction_cost}")

best_path, minimum_cost = tsp(cost)

print("\nOptimal Tour")
print("-" * 40)
print(" -> ".join(cities[i] for i in best_path))

print(f"\nMinimum Tour Cost = {minimum_cost}")

print("\nCost Calculation")
print("-" * 40)

total = 0
for i in range(len(best_path) - 1):
    u = best_path[i]
    v = best_path[i + 1]
    edge = cost[u][v]
    total += edge
    print(f"{cities[u]} -> {cities[v]} = {edge}")

print("-" * 40)
print(f"Total Cost = {total}")
