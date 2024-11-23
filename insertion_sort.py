
def insertion_sort(arr):
    init_counter = 0
    compare_counter = 0
    for j in range(1, len(arr)):
        i = j - 1
        key = arr[j]
        init_counter += 2

        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
            init_counter +=  2
            compare_counter += 1

        arr[i+1] = key
        init_counter += 1
    return compare_counter, init_counter




# def main():
#     arr = [43, 12, 32, 11, 21, 1, 2, 4, 6, 5, 78, 677]
#     compare_val, init_val = insertion_sort(arr)
#     print(f"Count of comparisions is: {compare_val}")
#     print(f"Count of initializations is: {init_val}")
#     print(arr)
#
# main()
