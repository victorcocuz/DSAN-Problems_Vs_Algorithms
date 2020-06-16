def sort_012(arr):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # Edge cases
    if len(arr) <= 1:
        return arr

    # Declare boundaries
    start, end = 0, len(arr) - 1
    index = 0

    # Go through the list once. Evaluate number at each index and narrow down boundaries
    while index <= end:
        # Move boundaries
        while arr[start] == 0:
            start += 1
        if index < start:
            index = start

        while arr[end] == 2:
            end -= 1

        # If number is 0, move at the beginning by using a temp variable
        if arr[index] == 0:
            temp = arr[start]
            arr[start] = arr[index]
            arr[index] = temp
        
        # If number is 2, move at the end by using a temp variable
        if arr[index] == 2:
            temp = arr[end]
            arr[end] = arr[index]
            arr[index] = temp

        # Move index
        if arr[index] == 1:
            index += 1
    return arr

# Test function
def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Tests
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Edge cases
test_function([])
test_function([0])
test_function([0, 1])
