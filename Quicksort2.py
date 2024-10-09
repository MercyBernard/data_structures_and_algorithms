def quicksort(arr, low, high):
  if low < high:
    #Partition the array and get the pivot
    pi = partition(arr, low, high)
    #Recursively sort elements before and after the partition
    quicksort(arr, low, pi - 1)
    quicksort(arr, pi + 1, high)

#Function to find the partition position
def partition(arr, low, high):
  pivot = arr[high] #Make the last element the pivot
  i = low #Pointer for greater elements
  j = high - 1 #Pointer for lesser elements

  while i < j:
    while i < high and arr[i] < pivot:
      i += 1 #Increment i when current element is less than pivot
    while j > low and arr[j] >= pivot:
      j -= 1 #Decrement j when current element is greater than pivot
    if i < j:
      arr[i], arr[j] = arr[j], arr[i] #Swap elements

  if arr[i] > pivot:
    arr[i], arr[high] = arr[high], arr[i] #Swap pivot to the correct position

  return i

#Function to remove duplicates from the sorted array
def remove_duplicates(arr):
    if not arr:
        return 0  # Edge case: empty array

    # Initialize a variable to keep track of the current index for unique elements
    unique_index = 0

    # Iterate through the array starting from the second element
    for i in range(0, len(arr)):
        # If current element is different from the previous unique element, move it to the next position
        if arr[i] != arr[unique_index]:
            unique_index += 1
            arr[unique_index] = arr[i]

    # Return the length of the array containing unique elements
    return unique_index + 1

Array = [50, 11, 33, 21, 40, 50, 40, 40, 21]
if len(Array) == 0:
  print("Empty array input case, so no output")
  result = 0

elif len(Array) == 1:
  print("Only one element in array, array is sorted")
  result = 1

else:
  quicksort(Array, 0, len(Array) - 1) #Sort the array
  result = remove_duplicates(Array)
# Print the array with unique elements
print("ARRAY =", Array[:result])
