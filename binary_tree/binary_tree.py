class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def insert(node, key):
    if node is None:
        return Node(key)  # cria um novo
    
    if key < node.value: # se o valor inserido for menor que o valor do nó atual
        node.left = insert(node.left, key)

    elif key > node.value: # maior que o valor do nó atual
        node.right = insert(node.right, key)
    else:
        print('Value already exists in tree')
    return node 

def count_nodes(node):
    if node is None:
        return 0
    
    left_nodes = count_nodes(node.left)
    right_nodes = count_nodes(node.right)
    total_nodes = left_nodes + right_nodes + 1 # soma com o nó atual

    return total_nodes

def count_leaves(node):
    if node is None:
        return 0
    
    if node.left is None and node.right is None: # verifica se não tem filhos(folha)
        return 1
    
    left_leaves = count_leaves(node.left)
    right_leaves = count_leaves(node.right)
    total_leaves = left_leaves + right_leaves

    return total_leaves

def search(node, key):
    if node is None or node.value == key:
        return node

    if key < node.value: # se o valor buscado for maior que o valor do nó atual, busca na esquerda
        return search(node.left, key)
    return search(node.right, key) # se for maior, busca na direita

def display_tree(current_node, level=0):
    if current_node is not None: # continua se o nó atual não for nulo
        display_tree(current_node.right, level + 1) # exibe o lado direito
        indent = ' ' * 4 * level # cria identacao para o nivel atual

        print(f'{indent}→ {current_node.value}')

        display_tree(current_node.left, level + 1) # exibe o lado esquerdo
