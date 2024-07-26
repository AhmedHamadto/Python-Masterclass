import numpy as np

def print_first_element(arr):
    print(arr[0])  # Accessing the first element of the array

# No matter how big the array is, it takes constant time to print the first element.


def find_element(arr, target):
    for element in arr:
        if element == target:
            return True
    return False

# In the worst case, the loop might need to iterate through the entire array to find the target.


def print_all_pairs(arr):
    for i in arr:
        for j in arr:
            for k in arr:
                print(i, j, k)


# As the array grows, the number of printed pairs increases quadratically with the input size.

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index

        if arr[mid] == target:  # Found the target element
            return mid
        elif arr[mid] < target:  # Target is in the right half
            low = mid + 1
        else:  # Target is in the left half
            high = mid - 1

    return -1  # Target not found in the array

# Example usage:
# my_array = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
# target_element = 23
# result = binary_search(my_array, target_element)
# if result != -1:
#     print(f"Element {target_element} found at index {result}.")
# else:
#     print(f"Element {target_element} not found in the array.")

a = np.array([1, 2, 3])
print_all_pairs(a)