def intersection(arr1, arr2):
    i, j = 0, 0  # Initialize two pointers for arr1 and arr2
    ARRAY = []  # Initialize the result array to store common elements

    # Traverse both arrays simultaneously
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:  # If elements at both pointers are equal
            if not ARRAY or ARRAY[-1] != arr1[i]:  # Check for duplicates
                ARRAY.append(arr1[i])  # Add the common element to the result array
            i += 1  # Move the pointer of arr1 forward
            j += 1  # Move the pointer of arr2 forward
        elif arr1[i] < arr2[j]:  # If element in arr1 is smaller
            i += 1  # Move the pointer of arr1 forward
        else:  # If element in arr2 is smaller
            j += 1  # Move the pointer of arr2 forward

    return ARRAY  # Return the result array

ARRAY1 = [1, 6, 9, 10, 11, 21]  # Define the first sorted array
ARRAY2 = [2, 6, 9, 11, 17, 21]  # Define the second sorted array

# Test case 1: Both arrays are empty
if len(ARRAY1) == 0 and len(ARRAY2) == 0:
    print("Empty arrays, cannot perform search ")

# Test case 2: The first array is empty
elif len(ARRAY1) == 0:
    print("ARRAY1 is empty, cannot perform search")

#Test case 3: Regular scenerio
else:
    print("ARRAY =", intersection(ARRAY1, ARRAY2))