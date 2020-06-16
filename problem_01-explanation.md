# Problem 1 - Explanation
## Strategy
Use binary search to calculate the square root of the number:
- Split the number in half
- Choose the middle of the number and check if the power of two is the closest to the number
- If smaller, choose the middle of the upper half and recurse
- If larger, choose the middle of lower half and recurse
- Stop when the number is found

## Time and Space Complexity
Time complexity: **O(log n)** - in a Binary Search, the search range reduces by half with each search, so in log n steps you find the result
Space complexity: **O(1)** - there is no need for extra resources, no matter how large the number.
