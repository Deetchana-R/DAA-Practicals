import random
import time

# Global Counters
comparison_count = 0
recursive_calls = 0


# ---------------- Divide and Conquer ----------------
def min_max_dc(arr, low, high):
    global comparison_count
    global recursive_calls

    recursive_calls += 1

    # Base Case - Single Element
    if low == high:
        return arr[low], arr[low]

    # Base Case - Two Elements
    if high == low + 1:
        comparison_count += 1

        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide
    mid = (low + high) // 2

    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)

    # Combine
    comparison_count += 1
    overall_min = lmin if lmin < rmin else rmin

    comparison_count += 1
    overall_max = lmax if lmax > rmax else rmax

    return overall_min, overall_max


# ---------------- Naive Method ----------------
def min_max_naive(arr):

    minimum = arr[0]
    maximum = arr[0]

    comparisons = 0

    for x in arr[1:]:

        comparisons += 1
        if x < minimum:
            minimum = x

        comparisons += 1
        if x > maximum:
            maximum = x

    return minimum, maximum, comparisons


# ---------------- Main Program ----------------

print("========== MINIMUM & MAXIMUM USING DIVIDE AND CONQUER ==========")

n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")

for i in range(n):
    value = int(input(f"Element {i + 1}: "))
    arr.append(value)

print("\nInput Array:")
print(arr)

comparison_count = 0
recursive_calls = 0

start = time.perf_counter()

dc_min, dc_max = min_max_dc(arr, 0, n - 1)

end = time.perf_counter()

dc_time = end - start

naive_min, naive_max, naive_comparisons = min_max_naive(arr)

print("\n---------------- RESULT ----------------")
print("Minimum Value :", dc_min)
print("Maximum Value :", dc_max)

print("\n----------- PERFORMANCE -----------")
print("Divide & Conquer Comparisons :", comparison_count)
print("Naive Comparisons             :", naive_comparisons)
print("Recursive Calls              :", recursive_calls)
print("Execution Time               : {:.8f} seconds".format(dc_time))

formula = (3 * n // 2) - 2

print("Theoretical Comparisons (3n/2 - 2):", formula)

print("\nVerification:")
if dc_min == naive_min and dc_max == naive_max:
    print("✔ Both methods produced the SAME result.")
else:
    print("✘ Results are different.")

print("\nProgram Executed Successfully.")
