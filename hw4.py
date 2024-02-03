import timeit
import random


# Timsort
def timsort_sort(array):
    return array.sort()

def timsort_sorted(array):
    return sorted(array)


# Insertion sort
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


# Merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Функціонал для тестування
def shuffled_list(n):
    numbers = list(range(1, n + 1))
    random.shuffle(numbers)
    return numbers

def sorting_speed_test(len):
    print(f'The length of the list: "{len}"')
    execution_time = timeit.timeit(lambda: timsort_sorted(shuffled_list(len)), number=1)
    print(f'Execution time "Timsort" (sorted): {execution_time}')
    execution_time = timeit.timeit(lambda: timsort_sort(shuffled_list(len)), number=1)
    print(f'Execution time "Timsort" (sort): {execution_time}')
    execution_time = timeit.timeit(lambda: merge_sort(shuffled_list(len)), number=1)
    print(f'Execution time "merge": {execution_time}')
    execution_time = timeit.timeit(lambda: insertion_sort(shuffled_list(len)), number=1)
    print(f'Execution time "insertion": {execution_time}')


# Тест
sorting_speed_test(10000)
sorting_speed_test(15000)
sorting_speed_test(20000)
sorting_speed_test(50000)