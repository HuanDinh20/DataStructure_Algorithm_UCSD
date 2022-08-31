"""
while low < high:
    middle = low + (high - low)/2
    if key == A[middle]:
        return mid
    elif key < A[middle]:
        high = middle - 1
    else:
        low = middle + 1
    return low - 1

O(log n )
"""


def binary_search(array, key, low, high):
    while low <= high:
        middle = low + (high - low)/2
        if key == array[middle]:
            return middle
        elif key < array[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return low - 1

