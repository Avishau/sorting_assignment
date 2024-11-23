from cProfile import label

import matplotlib.pyplot as plt
import random
from insertion_sort import insertion_sort
from heap_sort import heap_sort
from quick_sort import quick_sort
from merge_sort import merge_sort

def test_sorting_algorithms():
    algorithms = [insertion_sort, heap_sort, quick_sort, merge_sort]
    algorithms_names = ['insertion_sort', 'heap_sort', 'quick_sort', 'merge_sort']

    test_cases = [
        {"name": "Sorted Array", "arr": [2,3,5,6,7]},
        {"name": "Reverse Sorted Array", "arr": [6,5,4,3,1]},
        {"name": "Array With Duplications", "arr": [1,2,2,3,1,3,4]},
        {"name": "Mixed Integers and Floats", "arr": [1.7,2,3.4,6.3,1,5.5]},
        {"name": "Array of Positive Numbers", "arr": [1,2,3,4,5]},
        {"name": "Array with Negative Numbers", "arr": [-1,-4,4,5,6,-7]},
        {"name": "Random Array with Negative and Positive numbers", "arr": [random.randint(-100, 100) for _ in range(10)]}
    ]
    performance_data = {name: {"comparisons": [], "initializations": []} for name in algorithms_names}

    for case in test_cases:
        arr = case["arr"]
        for i, algo in enumerate(algorithms):
            arr_copy = arr.copy()
            comparisons, initializations = algo(arr_copy)
            performance_data[algorithms_names[i]]["comparisons"].append(comparisons)
            performance_data[algorithms_names[i]]["initializations"].append(initializations)
            print(f"{algorithms_names[i]} -Comparisons: {comparisons}, Initializations: {initializations}")

    return performance_data

def plot_performance(performance_data):
    fix, axs = plt.subplot(2,1, figsize=(10,10))

    for algo_name, data in performance_data.items():
        axs[0].plot(range(len(data["comparisons"])), data["comparisons"], label=algo_name)
        axs[0].set_title("Comparisons vs. Input Size")
        axs[0].set_xlabel("Input Size")
        axs[0].set_ylabel("Comparisons")
        axs[0].legend()

    for algo_name, data in performance_data.items():
        axs[1].plot(range(len(data["initializations"])), data["initializations"], label=algo_name)
        axs[1].set_title("Initializations vs. Input Size")
        axs[1].set_xlabel("Input Size")
        axs[1].set_ylabel("Initializations")
        axs[1].legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    performance_data = test_sorting_algorithms()
    plot_performance(performance_data)



# for sort_name, values in data.items():
#         plt.plot(list_lengths, values, label=sort_name)
#
#     plt.xlabel("Length of List")
#     plt.ylabel(f"Number of {metric.capitalize()}")
#     plt.title(f"Comparison of Quick Sort Variants - {metric.capitalize()}")
#     plt.legend()
#     plt.grid(True)
#     plt.show()