# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, entry):
        # Insert the node as before
        self.children[entry] = RouteTrieNode()
        return self.children[entry]
        

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = None

    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for entry in path_list:
            if entry not in current_node.children:
                current_node.insert(entry)
            current_node = current_node.children[entry]
        current_node.handler = handler
            

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for entry in path_list:
            if entry not in current_node.children:
                return
            current_node = current_node.children[entry]
        return current_node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, router_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routeTrie = RouteTrie()
        self.router_handler = router_handler
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.routeTrie.insert(self.split_path(path), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == '/':
            return self.router_handler

        handler = self.routeTrie.find(self.split_path(path))

        if handler is None:
            return self.not_found_handler

        return handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path[-1] == '/':
            path = path[:-1]
            
        return path.split('/')


# Tests
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
