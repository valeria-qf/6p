import binary_tree

if __name__ == '__main__':
    root = None
    tree_size = int(input('How many nodes would you like in your tree? \n'))
    
    print('Enter the values for the nodes:')
    for _ in range(tree_size):
        value = int(input(f'Node {_ + 1}: '))
        root = binary_tree.insert(root, value)  
    
    print('\n-----------------')
    binary_tree.display_tree(root)  
    
    print('\nTotal number of nodes in the tree:', binary_tree.count_nodes(root))
      
    print('Total number of leaves in the tree:', binary_tree.count_leaves(root))  
    
    search_key = int(input('Which value would you like to search for? \n'))
    found_node = binary_tree.search(root, search_key) 
    if found_node:
        print(f'\nNode {search_key} found!')
    else:
        print(f'\nNode {search_key} not found.')
