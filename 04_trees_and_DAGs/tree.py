# a tree is just a graph where each node is the child of only one parent node
# except for the root node, which has no parent

class TreeNode:
    def __init__(self, value, *children):
        self.value = value
        self.children = children

    def __str__(self):
        """Serialise the tree recursively as parent -> (children)."""
        childstring = ", ".join(map(str, self.children))
        return f"{self.value!s} -> ({childstring})"
    
# but we need to travel the tree in order to edit its nodes. 
# tree travelers are often called visitors

def postvisitor(tree, fn):
    """traverse tree in post-order applying a function to each node.
    post-order involves looking at leaves first, using their values for parent nodes,
    and so on until the root node is processed.
    """
    # recursively calls postvisitor on all of the children of the current node
    # *before* calling fn() on the current node
    return fn(tree, *(postvisitor(c, fn) for c in tree.children))

def previsitor(tree, fn, parent_fn_out=None):
    """traverse tree in pre-order applying a function to each node.
    pre-order involves looking at the current node first, using its value for its children,
    and so on until the leaf nodes are processed.
    """
    fn_out = fn(tree, parent_fn_out)
    for child in tree.children:
        previsitor(child, fn, fn_out)
    
if __name__ == "__main__":
    tree = TreeNode(
        "a",
        TreeNode("b", TreeNode("d"), TreeNode("e"), TreeNode("f")),
        TreeNode("c", TreeNode("g"))
    )
    print(tree)
    print('-'*40)
    
    # the postvisitor will sum the results from its children and add one for itself
    fn = lambda n, *c: sum(c) + 1
    print(postvisitor(tree, fn))
    print('-'*40)

    # with preorder traversal we can measure the depth in the tree of every node
    def fn(node, parent_fn_out):
        depth = parent_fn_out + 1 if parent_fn_out else 1
        print(f"{node.value!s} at depth {depth}")
        return depth
    previsitor(tree, fn)
    print('-'*40)

