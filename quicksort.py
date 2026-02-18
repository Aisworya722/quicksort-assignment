import random
from typing import List


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
    """
    Randomized Quicksort (in-place)
    """
    if hi is None:
        hi = len(a) - 1
    if lo >= hi:
        return

    pivot_index = random.randint(lo, hi)
    a[pivot_index], a[hi] = a[hi], a[pivot_index]

    p = partition_lomuto(a, lo, hi)
    quicksort_randomized(a, lo, p - 1)
    quicksort_randomized(a, p + 1, hi)


if __name__ == "__main__":
    data1 = [10, 7, 8, 9, 1, 5, 5, 2]
    data2 = data1.copy()

    quicksort_deterministic(data1)
    quicksort_randomized(data2)

    print("Deterministic:", data1)
    print("Randomized:   ", data2)
