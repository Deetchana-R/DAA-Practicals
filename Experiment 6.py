import time

cost_calculations = 0

def matrix_chain_order(dims):
    global cost_calculations
    n = len(dims) - 1
    m = [[0]*(n+1) for _ in range(n+1)]
    s = [[0]*(n+1) for _ in range(n+1)]

    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i+l-1
            m[i][j] = float("inf")
            for k in range(i, j):
                cost_calculations += 1
                cost = m[i][k] + m[k+1][j] + dims[i-1]*dims[k]*dims[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k
    return m, s

def optimal_parens(s, i, j):
    if i == j:
        return f"A{i}"
    k = s[i][j]
    return f"({optimal_parens(s,i,k)} x {optimal_parens(s,k+1,j)})"

def build_steps(s, i, j, steps):
    if i == j:
        return f"A{i}"
    k = s[i][j]
    left = build_steps(s, i, k, steps)
    right = build_steps(s, k+1, j, steps)
    expr = f"({left} x {right})"
    steps.append(f"Multiply {left} with {right} -> {expr}")
    return expr

def print_cost_table(m, n):
    print("\nDP COST TABLE")
    print("      ", end="")
    for j in range(1, n+1):
        print(f"A{j:>8}", end="")
    print()
    for i in range(1, n+1):
        print(f"A{i:<4} ", end="")
        for j in range(1, n+1):
            if j < i:
                print(f"{'-':>9}", end="")
            else:
                val = "∞" if m[i][j] == float("inf") else str(m[i][j])
                print(f"{val:>9}", end="")
        print()

def print_split_table(s, n):
    print("\nSPLIT TABLE")
    print("      ", end="")
    for j in range(1, n+1):
        print(f"A{j:>5}", end="")
    print()
    for i in range(1, n+1):
        print(f"A{i:<4} ", end="")
        for j in range(1, n+1):
            if j <= i:
                print(f"{'-':>6}", end="")
            else:
                print(f"{s[i][j]:>6}", end="")
        print()

def save_result(filename, text):
    with open(filename, "w") as f:
        f.write(text)

def run():
    global cost_calculations
    print("="*60)
    print(" MATRIX CHAIN MULTIPLICATION USING DYNAMIC PROGRAMMING")
    print("="*60)

    while True:
        try:
            n = int(input("Enter number of matrices (>=2): "))
            if n >= 2:
                break
            print("Minimum two matrices required.")
        except ValueError:
            print("Enter a valid integer.")

    dims = []
    print(f"\nEnter {n+1} dimensions:")
    for i in range(n+1):
        while True:
            try:
                d = int(input(f"Dimension {i+1}: "))
                if d > 0:
                    dims.append(d)
                    break
                print("Dimension must be positive.")
            except ValueError:
                print("Enter a valid integer.")

    print("\nMatrices:")
    for i in range(n):
        print(f"A{i+1}: {dims[i]} x {dims[i+1]}")

    cost_calculations = 0
    start = time.perf_counter()
    m, s = matrix_chain_order(dims)
    elapsed = time.perf_counter() - start

    print(f"\nTotal Matrices: {n}")
    print(f"Minimum Scalar Multiplications: {m[1][n]}")
    print("Optimal Parenthesization:", optimal_parens(s,1,n))

    print_cost_table(m,n)
    print_split_table(s,n)

    steps=[]
    build_steps(s,1,n,steps)
    print("\nSTEP-BY-STEP MULTIPLICATION ORDER")
    for idx, st in enumerate(steps,1):
        print(f"Step {idx}: {st}")

    print("\nPERFORMANCE")
    print(f"Execution Time : {elapsed:.8f} seconds")
    print(f"Cost Calculations : {cost_calculations}")
    print("Time Complexity : O(n^3)")
    print("Space Complexity: O(n^2)")
    print("\nVerification: Optimal Parenthesization Generated Successfully.")

    out = []
    out.append("Matrix Chain Multiplication Result\n")
    out.append(f"Dimensions: {dims}\n")
    out.append(f"Minimum Cost: {m[1][n]}\n")
    out.append(f"Optimal Parenthesization: {optimal_parens(s,1,n)}\n")
    out.append(f"Execution Time: {elapsed:.8f} seconds\n")
    out.append(f"Cost Calculations: {cost_calculations}\n")
    save_result("matrix_chain_result.txt","".join(out))
    print("\nResults saved to matrix_chain_result.txt")

while True:
    print("\nMENU")
    print("1. Run Matrix Chain Multiplication")
    print("2. Exit")
    ch = input("Enter your choice: ")
    if ch == "1":
        run()
    elif ch == "2":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
