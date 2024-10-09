def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: arrays with 0 or 1 element are already sorted
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
        left = [x for x in arr if x < pivot]  # Elements less than the pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
        right = [x for x in arr if x > pivot]  # Elements greater than the pivot
        return quick_sort(left) + middle + quick_sort(right)  # Recursively sort left and right parts and combine

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
print("Unsorted array:", arr)
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)



        