def quicksort(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)
    quicksort(arr, low, pi - 1)
    quicksort(arr, pi + 1, high)

def partition(arr, low, high):
  pivot = arr[high]
  i = low
  j = high - 1

  while i < j:
    while i < high and arr[i] < pivot:
      i += 1
    while j > low and arr[j] >= pivot:
      j -= 1
    if i < j:
      arr[i], arr[j] = arr[j], arr[i]

  if arr[i] > pivot:
    arr[i], arr[high] = arr[high], arr[i]

  return i
  

arr = [5]
if len(arr) == 0:
  print("Null input case, so no output")

elif len(arr) == 1:
  print("Array is already sorted")

else:
  quicksort(arr, 0, len(arr) - 1)
  print(arr)