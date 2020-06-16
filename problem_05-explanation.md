# Problem 1 - Explanation
## Strategy
Create a Trie that holds all the strings:
- Create a **Node** class for defining the node and its children, inserting a node and finding suffixes
- Create a **TrieNode** class that contains the root node, an insert and find function
- Implement each method
- For suffixes, declare a list and recursively go through all children of the given prefix, while keeping record of each car in a string. Each time a character has the property **is_word**, append the held string to the list. When the recursion ends, return the list.

## Time and Space Complexity
Time Complexity: 
- **O(n)** - where n is the number of characters in the word.
- **O(mn)** - for m words

Space Complexity: 
**O(mn)** - worst case scenario is having m words with n letters, where no word shares letters with another word