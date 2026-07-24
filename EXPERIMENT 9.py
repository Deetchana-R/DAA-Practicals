# Efficient Bin Packing using Approximation Algorithms

def first_fit_algorithm(objects, capacity):
    remaining_space = []
    packed_bins = []

    for obj in objects:
        inserted = False

        for i in range(len(remaining_space)):
            if remaining_space[i] >= obj:
                packed_bins[i].append(obj)
                remaining_space[i] -= obj
                inserted = True
                break

        if not inserted:
            packed_bins.append([obj])
            remaining_space.append(capacity - obj)

    return packed_bins


def first_fit_decreasing_algorithm(objects, capacity):
    sorted_objects = sorted(objects, reverse=True)
    return first_fit_algorithm(sorted_objects, capacity)


def best_fit_decreasing_algorithm(objects, capacity):
    sorted_objects = sorted(objects, reverse=True)

    packed_bins = []
    remaining_space = []

    for obj in sorted_objects:
        best_bin = -1
        minimum_space = float('inf')

        for i in range(len(remaining_space)):
            if remaining_space[i] >= obj:
                extra_space = remaining_space[i] - obj

                if extra_space < minimum_space:
                    minimum_space = extra_space
                    best_bin = i

        if best_bin == -1:
            packed_bins.append([obj])
            remaining_space.append(capacity - obj)
        else:
            packed_bins[best_bin].append(obj)
            remaining_space[best_bin] -= obj

    return packed_bins


def print_bins(title, bins, capacity):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    for i, b in enumerate(bins, start=1):
        used = sum(b)
        free = capacity - used

        print(f"Bin {i}")
        print(f"Items      : {b}")
        print(f"Used Space : {used:.1f}")
        print(f"Free Space : {free:.1f}")
        print("-" * 50)

    print(f"Total Bins Used = {len(bins)}")


# -------------------- MAIN PROGRAM --------------------

items = [0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]
capacity = 1.0

print("BIN PACKING USING APPROXIMATION ALGORITHMS")
print("=" * 50)

print("Items:")
print(items)

print(f"\nBin Capacity : {capacity}")

total_weight = sum(items)
lower_bound = int(-(-total_weight // capacity))

print(f"Total Weight : {total_weight}")
print(f"Minimum Possible Bins (Lower Bound): {lower_bound}")

ff_result = first_fit_algorithm(items, capacity)
ffd_result = first_fit_decreasing_algorithm(items, capacity)
bfd_result = best_fit_decreasing_algorithm(items, capacity)

print_bins("FIRST FIT (FF)", ff_result, capacity)
print_bins("FIRST FIT DECREASING (FFD)", ffd_result, capacity)
print_bins("BEST FIT DECREASING (BFD)", bfd_result, capacity)

print("\nSUMMARY")
print("=" * 50)
print(f"Lower Bound               : {lower_bound}")
print(f"First Fit                 : {len(ff_result)} bins")
print(f"First Fit Decreasing      : {len(ffd_result)} bins")
print(f"Best Fit Decreasing       : {len(bfd_result)} bins")
