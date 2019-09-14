# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with a root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root

        for part in path:
            node = node.insert(part)

        node.handler = handler

    def __repr__(self):
        return repr(self.root)

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root

        while len(path) > 0:
            part = path.pop(0)
            node = node.nodes.get(part)

            if node == None:
                return None

        return node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the` node with children as before, plus a handler
        self.nodes = dict()
        self.handler = None

    def insert(self, path_part):
        # Insert the node as before
        node = RouteTrieNode()
        self.nodes[path_part] = node
        return node

    def __repr__(self):
        return f"<Node handler='{self.handler}', nodes='{self.nodes}'"

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(root_handler)
        self.four_o_four = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if handler is None or path is None:
            return "Please add handler in the form 'add_handler(path, handler)'"

        path_arr = self.split_path(path)
        self.trie.insert(path_arr, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == "/" or path == "":
            return self.trie.root.handler

        path_arr = self.split_path(path)
        handler = self.trie.find(path_arr)

        if handler:
            return handler
        else:
            return self.four_o_four

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path[0] == "/":
            path = path[1:]

        split = path.split("/")
        sane = []
        for part in split:
            if part is not "":
                sane.append(part)

        return sane

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# # some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes

print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

# Edge Case - Empty path
print(router.lookup("")) # should print 'root handler'

# Edge Case - No handler
print(router.add_handler("/home/account/", None))
# Please add handler in the form 'add_handler(path, handler)'

# Edge Case - No path
print(router.add_handler(None, "account handler"))
# Please add handler in the form 'add_handler(path, handler)'
