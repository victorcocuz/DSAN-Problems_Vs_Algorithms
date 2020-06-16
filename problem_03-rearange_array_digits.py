def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Edge case
    if len(input_list) == 0:
        return [0, 0]
    if len(input_list) == 1:
        return [input_list[0], 0]

    return get_largest_sum(rearrange_digits_recursive(input_list))

# Helper method to return the largest sum of an ordered array
def get_largest_sum(arr):
    first, second = 0, 0

    # Alternatively appends digits to two different numbers in a descending order
    for i in range(len(arr)-1, -1, -2):
        if i >= 0:
            first *= 10 
            first += arr[i]
        if i - 1 >= 0:
            second *= 10
            second += arr[i-1]
    return [first, second]

# Recursive method that decomposes an array and sorts it by using Divide and Conquer
def rearrange_digits_recursive(input_list):
    if len(input_list) == 1:
        return input_list

    mid = len(input_list) // 2

    left = rearrange_digits_recursive(input_list[:mid])
    right = rearrange_digits_recursive(input_list[mid:])
    return sort(left, right)

# Helper method to merge-sort two arrays 
def sort(left, right):
    l = []
    left_index, right_index = 0, 0
    left_len, right_len = len(left), len(right)

    while left_index < left_len and right_index < right_len:
        if left[left_index] <= right[right_index]:
            l.append(left[left_index])
            left_index += 1
        else:
            l.append(right[right_index])
            right_index += 1
    
    if left_index >= left_len:
        l.extend(right[right_index:])
    else:
        l.extend(left[left_index:])
    return l
    
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Tests
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[4, 6, 2, 5, 9, 8, 3], [9642, 853]])
test_function([[4, 6, 2, 5, 9, 8, 3], [9642, 853]])

# Edge cases
test_function([[], [0]])
test_function([[1], [1]])
test_function([[1, 2], [2, 1]])
