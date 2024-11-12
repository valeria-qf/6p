from binary_heap.binary_heap import MaxBinaryHeap


if __name__ == "__main__":

    heap = MaxBinaryHeap()

    dados = [10, 5, 20, 1, 15, 30, 25]
    for valor in dados:
        heap.insert(valor)
    
    print("\nAlteração de Prioridade:")
    heap.change_priority(3, 50)
    heap.change_priority(1, 8)  
    
    print("\nRemoções:")
    for _ in range(3):
        heap.remove()
    
    print("\nHeapsort:")
    heap.heap_sort()
    
    high_priority = heap.get_high_priority()

    print(f'Elemento de alta prioridade: {high_priority}')