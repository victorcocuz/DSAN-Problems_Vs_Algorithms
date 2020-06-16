# Problem 1 - Explanation
## Strategy
Create a Trie that holds all the paths and handlers:
Create a **RouteTrieNode** class that contains:
- defines the node and its children and a handler
- an insert method to add a node
Create a **RouteTrieNode** class that contains:
- the root node and a handler
- an insert method to add a path list and a handler, by using the insert method in the RouteTrieNode
- a find method, using a path list to get a handler
Create a **Router** class that contains:
- a RouteTrie, the router handler and the not found handler
- a add_handler method that takes a path string as an input and adds it to the trie
- a lookup method that takes a path string as an input and uses it to traverse the trie
- a split_path method to split a path string into entries, by '/'

## Time and Space Complexity
- Time Complexity: **(O(n))** - for n entries after splitting the paths
- Space Complexity: **(o(n))** - worst case scenario is having n entries, where no entry is shared between paths
