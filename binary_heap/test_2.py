from binary_heap.binary_heap import MaxBinaryHeap


if __name__ == "__main__":


    heap = MaxBinaryHeap()
    for value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        heap.insert(value)

    print("\nAlteração de Prioridade:")
    heap.change_priority(7, 35)
    heap.change_priority(10, 12) 

    print("\nRemoções:")
    for _ in range(4):
        heap.remove()

    print("\nHeapsort:")
    heap.heap_sort()

    high_priority = heap.get_high_priority()
    print(f'Elemento de alta prioridade: {high_priority}')