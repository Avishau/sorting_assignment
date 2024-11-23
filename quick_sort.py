import random

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def randomized_partition(arr, start, end):
    randomized_index = random.randrange(start, end)
    swap(arr, randomized_index, end)
    return partition(arr, start, end)

def partition(arr, start, end):
    comparisons = 0
    initializations = 0
    pivot = arr[end]
    i = start - 1
    for j in range (start, end):
        if arr[j] <= pivot:
            comparisons += 1
            i += 1
            swap(arr, i, j)
            initializations += 2
    #i+1 is the correct index for the pivot in the array
    swap(arr, i+1, end)
    initializations += 1
    return i+1, initializations, comparisons


def quick_sort_rec(arr, start, end):
    if start >= end:
        return 0,0
    i1 = i2 = i3 = 0
    c1 = c2 = c3 = 0
    q, i1, c1 = randomized_partition(arr, start, end)
    i2, c2 = quick_sort_rec(arr, start, q-1)
    i3, c3 = quick_sort_rec(arr, q+1, end)

    initial_sum = i1 + i2 + i3
    comp_sum = c1 + c2 + c3
    return initial_sum, comp_sum

def quick_sort(arr):

    initializations, comparisons = quick_sort_rec(arr, 0, len(arr) - 1)
#     print(arr)
#     print(f"Number of comparisons is: {comparisons}")
#     print(f"Number of initializations is: {initializations}")
    return initializations, comparisons
#
# main()