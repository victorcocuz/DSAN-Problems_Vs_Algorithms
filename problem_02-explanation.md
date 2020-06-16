# Problem 1 - Explanation
## Strategy
Use Binary Search to successively split the array into equal parts and compare the middle element with the target:
- split array into equal parts and find the middle
- base case - if target is the middle, return the index
- implement recursion for either lower and upper half, depending on:
a. The relation of the target to the mid element
b. The relation of the target to the end of the array

## Time and Space Complexity
Time Complexity: **O(log(n))** for Binary Search
Space Complxity: **O(1)** as the space for the algorithm is not depending on the array size
