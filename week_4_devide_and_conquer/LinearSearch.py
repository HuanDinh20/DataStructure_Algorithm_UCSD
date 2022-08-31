"""
Pseudocode
def LinearSearch(array, key, low, high)
    for i in range (low, high):
        if a[i] = key:
            return i
        else:
            return Not_Found

Best case:

O(1)
O(n)
"""


def LinearSearch(array, key):
    for idx, value in enumerate(array):
        if value == key:
            return idx
        else:
            return None
