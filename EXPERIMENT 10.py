import random
import time
import sys

sys.setrecursionlimit(20000)


class QuickSortAnalyzer:
    def __init__(self):
        self.comparisons = 0

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            self.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def randomized_partition(self, arr, low, high):
        random_index = random.randint(low, high)
        arr[random_index], arr[high] = arr[high], arr[random_index]
        return self.partition(arr, low, high)

    def deterministic_quicksort(self, arr, low, high):
        if low < high:
            pivot = self.partition(arr, low, high)
            self.deterministic_quicksort(arr, low, pivot - 1)
            self.deterministic_quicksort(arr, pivot + 1, high)

    def randomized_quicksort(self, arr, low, high):
        if low < high:
            pivot = self.randomized_partition(arr, low, high)
            self.randomized_quicksort(arr, low, pivot - 1)
            self.randomized_quicksort(arr, pivot + 1, high)


def evaluate(sort_type, data):
    sorter = QuickSortAnalyzer()
    arr = data.copy()

    start = time.perf_counter()

    if sort_type == "Deterministic":
        sorter.deterministic_quicksort(arr, 0, len(arr) - 1)
    else:
        sorter.randomized_quicksort(arr, 0, len(arr) - 1)

    end = time.perf_counter()

    return sorter.comparisons, (end - start) * 1000


def generate_test_cases(size):
    cases = {
        "Random": [random.randint(1, 100000) for _ in range(size)],
        "Sorted": list(range(size)),
        "Reverse": list(range(size, 0, -1)),
        "Nearly Sorted": list(range(size))
    }

    # Shuffle 5% of elements
    nearly = cases["Nearly Sorted"]
    swaps = size // 20

    for _ in range(swaps):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        nearly[i], nearly[j] = nearly[j], nearly[i]

    return cases


def main():
    N = 5000
    test_cases = generate_test_cases(N)

    print("-" * 76)
    print(f"{'Input Type':<16}{'DQS Comparisons':>18}{'DQS Time(ms)':>16}"
          f"{'RQS Comparisons':>18}{'RQS Time(ms)':>16}")
    print("-" * 76)

    for case, arr in test_cases.items():

        d_comp, d_time = evaluate("Deterministic", arr)
        r_comp, r_time = evaluate("Randomized", arr)

        print(f"{case:<16}{d_comp:>18}{d_time:>16.2f}"
              f"{r_comp:>18}{r_time:>16.2f}")


if __name__ == "__main__":
    main()
