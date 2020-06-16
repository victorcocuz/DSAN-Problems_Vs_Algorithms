# Problem 1 - Explanation
## Strategy
Implement a quick sort algorithm:
- define a start and end boundary of the array
- define an index that traverses through the boundaries
- initially check how many 0s are on the left and how many 2s on the right and move the boundaries accordingly
- level the index boundary with the start boundary
- for each index, if it's a 0, swap the element with the element at the start value, or if it's a 2 with the lement at he end value

## Time and Space Complexity
Time Complexity: **O(n)** - The array is only traversed once, so time only increases linearly with the size of the array
Space Complexity: **O(1)** - The array is traversed in place, no extra data structures required.
