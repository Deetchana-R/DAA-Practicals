import time
import random


# ---------------- Interpolation Search ----------------
def interpolation_search(arr, target):

    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:

        # Avoid division by zero
        if arr[high] == arr[low]:

            comparisons += 1

            if arr[low] == target:
                return low, comparisons

            return -1, comparisons

        comparisons += 1

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos, comparisons

        elif arr[pos] < target:
            low = pos + 1

        else:
            high = pos - 1

    return -1, comparisons


# ---------------- Binary Search ----------------
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:

        comparisons += 1

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comparisons


# ---------------- Main Program ----------------

print("========== INTERPOLATION SEARCH ==========")

n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")

for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

arr.sort()

print("\nSorted Array:")
print(arr)

target = int(input("\nEnter element to search: "))

# Interpolation Search
start = time.perf_counter()

index_is, comp_is = interpolation_search(arr, target)

end = time.perf_counter()

time_is = (end - start) * 1000

# Binary Search
start = time.perf_counter()

index_bs, comp_bs = binary_search(arr, target)

end = time.perf_counter()

time_bs = (end - start) * 1000

# ---------------- Output ----------------

print("\n========== RESULT ==========")

if index_is != -1:
    print(f"Element found at index : {index_is}")
else:
    print("Element not found.")

print("\n------ Performance Comparison ------")
print(f"Interpolation Search Time : {time_is:.6f} ms")
print(f"Binary Search Time        : {time_bs:.6f} ms")
print(f"Interpolation Comparisons : {comp_is}")
print(f"Binary Comparisons        : {comp_bs}")

print("\nVerification")

if index_is == index_bs:
    print("✔ Both algorithms returned the SAME result.")
else:
    print("✘ Results are different.")

print("\nTime Complexity")
print("Best Case    : O(1)")
print("Average Case : O(log log n)")
print("Worst Case   : O(n)")

print("\nSpace Complexity : O(1)")

print("\nProgram Executed Successfully.")
