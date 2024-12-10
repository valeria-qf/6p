class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def insert(node, key):
    if node is None:
        return Node(key)  # Create a new node if none exists.
    
    if key < node.value:
        node.left = insert(node.left, key)  # Insert on the left subtree.
    elif key > node.value:
        node.right = insert(node.right, key)  # Insert on the right subtree.
    else:
        print('Value already exists in tree')
    return node  # Make sure to return the node to update the tree.

def count_nodes(node):
    if node is None:
        return 0
    
    left_nodes = count_nodes(node.left)
    right_nodes = count_nodes(node.right)
    total_nodes = left_nodes + right_nodes + 1

    return total_nodes

def count_leaves(node):
    if node is None:
        return 0
    
    if node.left is None and node.right is None:
        return 1
    
    left_leaves = count_leaves(node.left)
    right_leaves = count_leaves(node.right)
    total_leaves = left_leaves + right_leaves

    return total_leaves

def search(node, key):
    if node is None or node.value == key:
        return node

    if key < node.value:
        return search(node.left, key)
    return search(node.right, key)

def display_tree(current_node, level=0):
    if current_node is not None:
        display_tree(current_node.right, level + 1)
        indent = ' ' * 4 * level

        print(f'{indent}→ {current_node.value}')

        display_tree(current_node.left, level + 1)
