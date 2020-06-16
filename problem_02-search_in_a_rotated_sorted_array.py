def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Edge cases
    if len(input_list) == 0:
        return -1
    if len(input_list) == 1:
        return 0

    return rotated_array_search_recursive(input_list, number, 0)

# Recursive method that finds the index of a target 
# by using Divide and Conquer to successively split the array into equal parts and compare the middle element with the target
def rotated_array_search_recursive(arr, target, left):
    mid = (len(arr) - 1) // 2
    elem = arr[mid]

    # Base case
    if elem == target:
        return left + mid
    elif len(arr) == 1:
        return -1

    # Recursion
    elif elem > target:
        if arr[0] <= target:
            return rotated_array_search_recursive(arr[:mid], target, left)
        else:
            return rotated_array_search_recursive(arr[mid+1:], target, left + mid + 1)
    elif arr[len(arr) - 1] >= target:
        return rotated_array_search_recursive(arr[mid+1:], target, left + mid + 1)
    else: 
        return rotated_array_search_recursive(arr[:mid], target, left)


# Test functions
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Tests
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])

# Edge Case
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[1], 1])
test_function([[], None])
