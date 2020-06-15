def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """    
    # Edge cases
    if number < 0:
        return
    elif number <= 1:
        return number

    test = sqrt_floor(number, 0, number)
    return test

# Helper method to recursively look for the correct mid
def sqrt_floor(number, min, max):
    mid = (min + max) // 2
    square = mid ** 2
    if square <= number and (mid + 1) ** 2 > number:
        return mid
    elif square > number:
        return sqrt_floor(number, 0, mid)
    else:
        return sqrt_floor(number, mid, max)


# Test Cases
print("Pass" if (22 == sqrt(500)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (2 == sqrt(4)) else "Fail")

# Edge Cases
print("Pass" if (None == sqrt(-1)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
