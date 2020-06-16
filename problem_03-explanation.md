# Problem 1 - Explanation
## Strategy
Use Divide and Conquer to:
- Recursively break the array into individual arrays of length 1
- Combine these arrays successively with a helper function until a fully ordered array is returned

Having an ordered list, simply run through the list once and compose two sums, by alternatively adding digits to two different numbers in the descending order of the array

## Time and Space Complexity
Time Complexity:
- **T(nlog(n))** - Divide and Conquer
- **T(n)** - Traversing the array once
- **T(nlog(n)) + T(n) = O(nlog(n))** 

Space Complexity:
- **T(n)** - Divide and Conquer
- **T(n)** - Array
- **T(n) + T(n) = O(n)** 