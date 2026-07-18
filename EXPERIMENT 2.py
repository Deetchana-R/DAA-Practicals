import time
import random


# ---------------- Naive Search ----------------
def naive_search(text, pattern):

    n = len(text)
    m = len(pattern)

    matches = []
    comparisons = 0

    for i in range(n - m + 1):

        j = 0

        while j < m:

            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons


# ---------------- Compute LPS ----------------
def compute_lps(pattern):

    m = len(pattern)

    lps = [0] * m

    length = 0
    i = 1

    while i < m:

        if pattern[i] == pattern[length]:

            length += 1
            lps[i] = length
            i += 1

        elif length != 0:

            length = lps[length - 1]

        else:

            lps[i] = 0
            i += 1

    return lps


# ---------------- KMP Search ----------------
def kmp_search(text, pattern):

    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    matches = []
    comparisons = 0

    i = 0
    j = 0

    while i < n:

        comparisons += 1

        if text[i] == pattern[j]:

            i += 1
            j += 1

        if j == m:

            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:

            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons, lps


# ---------------- Rabin-Karp ----------------
def rabin_karp(text, pattern, q=101):

    d = 256

    n = len(text)
    m = len(pattern)

    h = pow(d, m - 1, q)

    pattern_hash = 0
    text_hash = 0

    matches = []
    comparisons = 0

    for i in range(m):

        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    for s in range(n - m + 1):

        if pattern_hash == text_hash:

            for k in range(m):

                comparisons += 1

                if text[s + k] != pattern[k]:
                    break

            else:
                matches.append(s)

        if s < n - m:

            text_hash = (
                d * (text_hash - ord(text[s]) * h)
                + ord(text[s + m])
            ) % q

            if text_hash < 0:
                text_hash += q

    return matches, comparisons


# ---------------- Main ----------------

print("========== STRING MATCHING ALGORITHMS ==========")

text = input("Enter Text    : ")
pattern = input("Enter Pattern : ")

if len(pattern) > len(text):
    print("\nPattern length cannot be greater than Text length.")
    exit()

# Naive
start = time.perf_counter()
m1, c1 = naive_search(text, pattern)
naive_time = (time.perf_counter() - start) * 1000

# KMP
start = time.perf_counter()
m2, c2, lps = kmp_search(text, pattern)
kmp_time = (time.perf_counter() - start) * 1000

# Rabin-Karp
start = time.perf_counter()
m3, c3 = rabin_karp(text, pattern)
rk_time = (time.perf_counter() - start) * 1000


print("\n========== RESULTS ==========")

print("Naive Search")
print("Matches      :", m1)
print("Comparisons  :", c1)
print("Time         : {:.6f} ms".format(naive_time))

print("\nKMP Search")
print("Matches      :", m2)
print("Comparisons  :", c2)
print("LPS Array    :", lps)
print("Time         : {:.6f} ms".format(kmp_time))

print("\nRabin-Karp")
print("Matches      :", m3)
print("Comparisons  :", c3)
print("Time         : {:.6f} ms".format(rk_time))

print("\nVerification")

if m1 == m2 == m3:
    print("✔ All algorithms produced the SAME result.")
else:
    print("✘ Results are different.")

print("\n------ Time Complexity ------")
print("Naive       : Best O(n), Worst O(nm)")
print("KMP         : O(n + m)")
print("Rabin-Karp  : Average O(n + m), Worst O(nm)")

print("\nProgram Executed Successfully.")
