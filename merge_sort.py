import random


def merge(arr, l , mid, r):
    i = j = 0
    k = l
    init_counter_of_merge = 0
    compare_counter_of_merge = 0
    left_arr = arr[l:mid+1]
    right_arr = arr[mid+1:r+1]
    length_sub_left_arr = len(left_arr)
    length_sub_right_arr = len(right_arr)
    while i < length_sub_left_arr and j < length_sub_right_arr:
        compare_counter_of_merge += 1
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        init_counter_of_merge += 1
        compare_counter_of_merge += 1
        k += 1

    while i < length_sub_left_arr:
        compare_counter_of_merge += 1
        arr[k] = left_arr[i]
        init_counter_of_merge += 1
        k += 1
        i += 1

    return init_counter_of_merge, compare_counter_of_merge

    



def merge_sort_recursive(arr, l, r):
    if l == r:
        return 0, 0
    mid = (l+r)//2

    i1, c1 = merge_sort_recursive(arr, l, mid)
    i2, c2 = merge_sort_recursive(arr, mid + 1, r)
    i3, c3 = merge(arr, l, mid, r)
    init_counter_sum = i1 + i2 + i3
    compare_counter_sum = c1 + c2 + c3

    return init_counter_sum, compare_counter_sum

def merge_sort(arr):
    end = len(arr)
    start = 0
    init_val, compare_val = merge_sort_recursive(arr, start, end-1)
    return init_val, compare_val


# def test_merge_sort():
#     sizes = [1000, 10000, 100000]
#     passed = True
#     for size in sizes:
#         test_arr = [random.uniform(-2000,20000) for _ in range(size)]
#         test_arr_copy = test_arr[:]
#         comp, init = merge_sort(test_arr)
#         print(test_arr[:20])
#         print(f"Number of comparissions is: {comp}")
#         print(f"Number of initiallization is: {init}")
#         passed = passed and test_arr == sorted(test_arr_copy)
#         print(passed)
#     return passed
#
# test_merge_sort()
#
#
#
