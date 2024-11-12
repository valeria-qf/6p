class MaxBinaryHeap:
    def __init__(self):
        self.heap = [None]  # posição 0 mantida vazia
    
    def heapify_up(self, index):
        # Enquanto o índice não for a raiz (1)
        while index > 1:
            parent_index = index // 2

            # Verifica se o valor do nó atual é maior que o valor do nó pai
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def heapify_down(self, index, heap=None):
        # Se heap não for fornecido, usa self.heap por padrão
        if heap is None:
            heap = self.heap

        heap_size = len(heap)

        while True:
            left_child_index = 2 * index
            right_child_index = (2 * index) + 1
            largest = index

            # Se um dos filhos for maior que o valor atual, o valor desce até o nó filho com o maior valor
            if left_child_index < heap_size and heap[left_child_index] > heap[largest]:
                largest = left_child_index

            if right_child_index < heap_size and heap[right_child_index] > heap[largest]:
                largest = right_child_index
            
            if largest != index:
                # Troca os valores entre o nó atual e o maior dos filhos
                heap[index], heap[largest] = heap[largest], heap[index]
                index = largest
            else:
                break

    def insert(self, value):
        self.heap.append(value)
        last_index = len(self.heap) - 1  # ultimo elemento
        
        self.heapify_up(last_index)
        print('Estado do heap após inserir', value, ':', self.heap[1:])

    def remove(self):
        if len(self.heap) <= 1:
            return None
        
        max_value = self.heap[1]
        self.heap[1] = self.heap[-1]  # substitui a raiz pelo último valor da lista
        self.heap.pop()

        self.heapify_down(1)  # Ordena
        print('Estado do heap após remoção do elemento de alta prioridade:', self.heap[1:])
        return max_value

    def change_priority(self, index, new_priority):
        if index < 1 or index >= len(self.heap):
            print("Índice fora dos limites.")
            return
        
        old_priority = self.heap[index]
        self.heap[index] = new_priority

        # Se a nova prioridade for maior que a antiga, o elemento precisa subir no heap
        if new_priority > old_priority:
            self.heapify_up(index)
        else:
            # Se a nova prioridade for menor que a antiga, o elemento precisa descer no heap
            self.heapify_down(index)
        print(f'Estado do heap após alteração de prioridade do índice {index} para {new_priority}:', self.heap[1:])

    def get_high_priority(self):
        return self.heap[1] if len(self.heap) > 1 else None

    def heap_sort(self):
        # copia do heap original para preservar o estado, incluindo um espaço vazio na posição 0
        heap_copy = [None] + self.heap[1:]  # ignorar a posição 0
        sorted_list = []

        # ordena os elementos removendo a raiz (maior) repetidamente
        while len(heap_copy) > 1:  # enquanto houver elementos no heap 
            print("Estado atual do heap antes da remoção:", heap_copy[1:])
            
            # Adiciona a raiz (heap_copy[1]) na lista ordenada
            sorted_list.append(heap_copy[1])

            # troca o ultimo elemento para a raiz e remove o maior
            heap_copy[1] = heap_copy[-1]
            heap_copy.pop()

            # reorganiza o heap para manter a propriedade de MaxHeap, iniciando da raiz (índice 1)
            self.heapify_down(index=1, heap=heap_copy)
            print("Estado do heap após reorganização:", heap_copy[1:])
        
        print("Heap ordenado:", sorted_list)
        return sorted_list 


    def display_heap(self):
        print('Estado atual do heap:', self.heap[1:])
