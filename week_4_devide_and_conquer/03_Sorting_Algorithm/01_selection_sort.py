"""
always
O(n^2)

Pseudocode:

Selection_sort:
    for i in range len(array):
        min_idx = i
        for j in range(min_idx+1, len(array))
            if array[j] < array[min_idx]:
                min_idx = i

        array[min_idx], array[i] = array[i], array[min_idx]
"""


def selection_sort(array):
    size = len(array)
    for step in range(size):
        min_idx = step
        for further_step in range(step+1, size):
            if array[further_step] < array[min_idx]:
                min_idx = further_step
        array[min_idx], array[step] = array[step], array[min_idx]


data = [-2, 45, 0, 11, -9]
size = len(data)
selection_sort(data)
print('Sorted Array in Ascending Order:')
print(data)