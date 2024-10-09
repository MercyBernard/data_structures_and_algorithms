arr = [2, 4, 1, 5, 6, 9, 7, 3, 8]
target = 6

def linear_search(arr, target):
    for i in arr:
        if arr[i] == target:
            return i
        
    return -1

result = linear_search(arr, target)
if result == -1:
    print("Target not found")
else:
    print("Target found at index", result)
    