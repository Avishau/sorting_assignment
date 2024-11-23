import random

def parent (i):
    return (i-1)/2
def left_son(i):
    return 2*i + 1
def right_son(i):
    return 2*i + 2

def max_heapify(arr, i, heap_size):
    initializations = comparisons = 0
    initializations_sum = comparisons_sum = 0
    left = left_son(i)
    right = right_son(i)
    largest = i
    if left <= heap_size and arr[left] > arr[i]:
        comparisons += 1
        largest = left
    if right <= heap_size and arr[right] > arr[largest]:
        comparisons += 1
        largest = right
    if largest != i:
        exchange(arr, i, largest)
        initializations += 3
        initializations_sum += initializations
        comparisons_sum += comparisons
        initializations, comparisons = max_heapify(arr, largest, heap_size)
        initializations_sum += initializations
        comparisons_sum += comparisons
    return initializations_sum, comparisons_sum


def build_max_heap(arr, heap_size):
    mid = (len(arr) - 1) // 2
    i_sum = c_sum = 0
    # i2 = c2 = 0
    for father in range(mid, -1, -1):
        i2, c2 = max_heapify(arr, father, heap_size)
        i_sum += i2
        c_sum += c2
    return i_sum, c_sum




def exchange(arr, first, last):
    temp = arr[first]
    arr[first] = arr[last]
    arr[last] = temp

    #arr[first], arr[last] = arr[last], arr[first]

def heap_sort(arr):
    n = heap_size = len(arr) - 1
    # init1 = compare1 = 0
    init_sum = compare_sum = 0
    init1, compare1 = build_max_heap(arr, heap_size)
    # init2 = compare2 = 0
    for i in range(n, 0, -1):
        exchange(arr, 0, i)
        init1 += 3
        heap_size -= 1
        init2, compare2 = max_heapify(arr, 0, heap_size)
        init_sum = init1 + init2
        compare_sum = compare1 + compare2

    return init_sum, compare_sum

# def main():
#     arr = [random.randint(-100, 100) for _ in range(10)]
#     print(f"The array before Heapsort: \n")
#     print(arr)
#     initializations, comparisons = heap_sort(arr)
#
#     print(f"The array after Heapsort: \n")
#     #heap_sort(arr)
#     print(arr)
#     print(f"Number of comparisons is: {comparisons}")
#     print(f"Number of initializations is: {initializations}")


# main()












