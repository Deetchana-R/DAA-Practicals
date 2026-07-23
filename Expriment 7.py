import time

safe_checks = 0
recursive_calls = 0
backtrack_count = 0

def is_safe(board, row, col):
    global safe_checks
    safe_checks += 1
    for prev_row in range(row):
        placed = board[prev_row]
        if placed == col:
            return False
        if abs(prev_row-row) == abs(placed-col):
            return False
    return True

def solve_n_queens(n):
    global recursive_calls, backtrack_count
    board = [-1]*n
    solutions = []

    def backtrack(row):
        global recursive_calls, backtrack_count
        recursive_calls += 1

        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board,row,col):
                board[row]=col
                backtrack(row+1)
                board[row]=-1
                backtrack_count += 1

    backtrack(0)
    return solutions

def display_board(solution,n):
    print("  +"+"---+"*n)
    for r in range(n):
        print("  |",end="")
        for c in range(n):
            if solution[r]==c:
                print(" Q |",end="")
            else:
                print(" . |",end="")
        print()
        print("  +"+"---+"*n)

def queen_positions(solution):
    print("Queen Positions")
    for r,c in enumerate(solution):
        print(f"Row {r} -> Column {c}")

def save_result(filename,n,solutions,elapsed):
    with open(filename,"w") as f:
        f.write("N-Queens Result\n")
        f.write(f"N = {n}\n")
        f.write(f"Solutions = {len(solutions)}\n")
        f.write(f"Recursive Calls = {recursive_calls}\n")
        f.write(f"Safe Checks = {safe_checks}\n")
        f.write(f"Backtracks = {backtrack_count}\n")
        f.write(f"Execution Time = {elapsed:.8f} seconds\n")

def run():
    global safe_checks, recursive_calls, backtrack_count
    while True:
        try:
            n=int(input("Enter value of N (>=4): "))
            if n>=4:
                break
            print("N must be at least 4.")
        except ValueError:
            print("Enter a valid integer.")

    safe_checks=0
    recursive_calls=0
    backtrack_count=0

    start=time.perf_counter()
    solutions=solve_n_queens(n)
    elapsed=time.perf_counter()-start

    print("\n========== RESULTS ==========")
    print("Total Solutions :",len(solutions))
    print("Backtracks      :",backtrack_count)
    print("Recursive Calls :",recursive_calls)
    print("Safe Checks     :",safe_checks)
    print(f"Execution Time  : {elapsed:.8f} seconds")

    if n<=6:
        for i,sol in enumerate(solutions,1):
            print(f"\nSolution {i}: {sol}")
            queen_positions(sol)
            display_board(sol,n)
    else:
        if solutions:
            print("\nFirst Solution:")
            queen_positions(solutions[0])
            display_board(solutions[0],n)

    print("\nTime Complexity : O(N!)")
    print("Space Complexity: O(N)")
    print("Verification    : Solution Generated Successfully")

    save_result("nqueen_result.txt",n,solutions,elapsed)
    print("\nResults saved to nqueen_result.txt")

while True:
    print("\n========== N-QUEENS MENU ==========")
    print("1. Solve N-Queens")
    print("2. Exit")
    ch=input("Enter your choice: ")

    if ch=="1":
        run()
    elif ch=="2":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
