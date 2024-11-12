from binary_heap import MaxBinaryHeap


if __name__ == "__main__":


    heap = MaxBinaryHeap()
    for value in [13, 26, 19, 17, 24, 31, 22, 11, 8, 20, 5, 27, 18]:
        heap.insert(value)

    print("\nAlteração de Prioridade:")
    heap.change_priority(4, 15)  
    heap.change_priority(8, 3)   

    print("\nRemoções:")
    for _ in range(5):
        heap.remove()

    print("\nHeapsort:")
    heap.heap_sort()

    high_priority = heap.get_high_priority()
    print(f'Elemento de alta prioridade: {high_priority}')