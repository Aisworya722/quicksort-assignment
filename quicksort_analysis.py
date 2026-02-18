import sys
sys.setrecursionlimit(10000)


import random
import time
from typing import List


# ---------- Quicksort Functions ----------

def partition_lomuto(a: List[int], lo: int, hi: int) -> int:
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i


def quicksort_deterministic(a: List[int], lo: int = 0, hi: int | None = None) -> None:
    if hi is None:
        hi = len(a) - 1
    if lo >= hi:
        return

    p = partition_lomuto(a, lo, hi)
    quicksort_deterministic(a, lo, p - 1)
    quicksort_deterministic(a, p + 1, hi)


def quicksort_randomized(a: List[int], lo: int = 0, hi: int | None = None) -> None:
    if hi is None:
        hi = len(a) - 1
    if lo >= hi:
        return

    pivot_index = random.randint(lo, hi)
    a[pivot_index], a[hi] = a[hi], a[pivot_index]

    p = partition_lomuto(a, lo, hi)
    quicksort_randomized(a, lo, p - 1)
    quicksort_randomized(a, p + 1, hi)


# ---------- Timing Helper ----------

def measure_time(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr)
    end = time.perf_counter()
    return end - start


# ---------- Generate Test Data ----------

def run_experiments():
    sizes = [1000, 3000, 5000]

    for n in sizes:
        print(f"\n=== Size: {n} ===")

        random_arr = [random.randint(0, 10000) for _ in range(n)]
        sorted_arr = sorted(random_arr)
        reversed_arr = sorted_arr[::-1]

        for name, base in [
            ("Random", random_arr),
            ("Sorted", sorted_arr),
            ("Reversed", reversed_arr),
        ]:
            arr1 = base.copy()
            arr2 = base.copy()

            t1 = measure_time(quicksort_deterministic, arr1)
            t2 = measure_time(quicksort_randomized, arr2)

            print(f"{name:8} | Deterministic: {t1:.6f}s | Randomized: {t2:.6f}s")


if __name__ == "__main__":
    run_experiments()
