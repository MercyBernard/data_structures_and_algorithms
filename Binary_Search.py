arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 90
low = 0
high = len(arr) - 1

def binary_search(arr, target, low, high):
    while low <= high:
        mid = low + ((high - low)//2)

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1

result = binary_search(arr, target, low, high)
if result != -1:
    print("Target found at index", result)
else:
    print("Target not found in the array")
