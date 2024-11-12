from binary_heap.binary_heap import MaxBinaryHeap


if __name__ == "__main__":


    heap = MaxBinaryHeap()
    for value in [50, 40, 30, 20, 10, 5, 3]:
        heap.insert(value)


    print("\nAlteração de Prioridade:")
    heap.change_priority(2, 60)  
    heap.change_priority(5, 1) 
    
    print("\nRemoções:")
    for _ in range(3):
        heap.remove()
 
    print("\nHeapsort:")
    heap.heap_sort()
    

    high_priority = heap.get_high_priority()
    print(f'Elemento de alta prioridade: {high_priority}')